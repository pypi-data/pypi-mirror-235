"""
TODO:
- [X] Evaluation Metrics Design
    - [X] F1-Score / Precision / Recall should work on whole Regex
- [X] Add LLMChain to fix the regex with low F1 scores (done by iterative calling).
- [ ] Consider continual inferencing mode: statistics should evaluate on the future cases.
"""
import typing
from typing import List, Optional, Dict
import re
from .filter import Filter
from .chain import Chain
from ..utils import make_verbose


class Engine:
    def __init__(self, openai_api_key: Optional[str] = None, temperature: float = 0.8,
                 mismatch_tolerance: float = 0.1, max_iteration: int = 3, simpify_regex: bool = True, verbose: bool = False):
        self._chain = Chain(
            openai_api_key=openai_api_key,
            temperature=temperature)
        self._mismatch_tolerance = mismatch_tolerance
        self._max_iteration = max_iteration
        self._simpify_regex = simpify_regex
        if verbose:
            self._make_verbose()
        self._verbose = verbose

    @typing.no_type_check
    def _make_verbose(self):
        self.run = make_verbose(self.run)
        self._run_new_inference = make_verbose(self._run_new_inference)
        self._fix_regex = make_verbose(self._fix_regex)

    def run(self, patterns: List[str]) -> str:
        regex_list = self.get_regex_sequence(patterns)
        return Engine.merge_regex_sequence(regex_list)

    def get_regex_sequence(self, patterns: List[str]) -> List[str]:
        assert len(
            patterns) > 0, '`patterns` input to `run` should no be an empty list'
        regex_list = [self._run_new_inference(patterns)]
        mismatched_patterns = Filter.mismatch(
            Engine.merge_regex_sequence(regex_list),
            patterns
        )
        while mismatched_patterns:
            regex = self._run_new_inference(mismatched_patterns)
            regex_list.append(regex)
            mismatched_patterns = Filter.mismatch(
                Engine.merge_regex_sequence(regex_list), patterns)
        return regex_list

    def _run_new_inference(self, patterns: List[str]) -> str:
        for _ in range(self._max_iteration):
            result = self._chain.inference_regex.run(
                Engine._convert_patterns_to_prompt(patterns)
            ).strip()
            try:
                re.compile(result)
                return result
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
        raise ValueError(
            f'Unable to find inferred regex after {self._max_iteration} tries.')

    @staticmethod
    def _convert_patterns_to_prompt(patterns: List[str]) -> str:
        return '\n'.join(map(lambda x: f'"{x}"', patterns))

    @staticmethod
    def merge_regex_sequence(regex_list: List[str]) -> str:
        if len(regex_list) > 1:
            return '|'.join(map(lambda x: f'({x})', regex_list))
        elif len(regex_list) == 1:
            return regex_list[0]
        else:
            return ''

    def explain(self, regex: str) -> None:
        result = self._chain.explain_regex.run(regex)
        print(result)

    @staticmethod
    def get_correction_data(
            regex_list: List[str], patterns: List[str]) -> Dict[str, Dict[str, List[str]]]:
        """
        Args:
            - regex_list: the inference list of regex
            - the target patterns

        Returns:
            - correction_data (dict)
                - key: regex
                - value (dict)
                    - fields:
                        - correct
                        - incorrect
        """
        divided_patterns = Engine.divide_patterns(regex_list, patterns)
        result = dict()
        for i, regex in enumerate(regex_list):
            matched_patterns = Filter.match(regex_list[i], patterns)
            correct_patterns = divided_patterns[i]
            incorrect_patterns = list(
                set(matched_patterns) -
                set(correct_patterns))
            result[regex] = {
                'correct': correct_patterns,
                'incorrect': incorrect_patterns
            }
        return result

    @staticmethod
    def divide_patterns(regex_list: List[str],
                        patterns: List[str]) -> List[List[str]]:
        """
        Seperate a list of patterns to match the regex in regex_list
        """
        results = []
        for regex in regex_list:
            results.append(Filter.match(regex, patterns))
            patterns = Filter.mismatch(regex, patterns)
        return results

    def fix_regex_list(
            self, regex_list: List[str], correction_data: Dict[str, Dict[str, List[str]]]) -> List[str]:
        for i, regex in enumerate(regex_list):
            regex_list[i] = self.fix_regex(regex, correction_data)
        return regex_list

    def fix_regex(self, regex: str,
                  correction_data: Dict[str, Dict[str, List[str]]]) -> str:
        for _ in range(self._max_iteration):
            try:
                result = self._fix_regex(regex, correction_data)
                re.compile(result)
                break
            except KeyboardInterrupt as e:
                raise e
            except (ValueError, AssertionError):
                pass
        return result

    def _fix_regex(self, regex: str,
                   correction_data: Dict[str, Dict[str, List[str]]]) -> str:
        """
        Args:
            - regex_list: a list of regex to be fixed
            - correction_data: output of `get_correction_data`
        Return
            - fixed_regex_list: the corrected regex
        """
        regex_list = [regex]
        correct_patterns = [correction_data[regex]['correct']
                            for regex in regex_list]
        incorrect_patterns = [correction_data[regex]
                              ['incorrect'] for regex in regex_list]
        cnt = len(regex_list)
        fact_0_str = f"""
Fact 0:

A list of regex describing {cnt} type of patterns is double quoted and shown as the following bullet points:
    """
        regex_list_str = "\n".join(
            map(lambda x: f'{x[0]+1}. "{x[1]}"', enumerate(regex_list)))

        facts = "\n\n".join(map(lambda i: f"""
Fact {i+1}

For regex number {i+1}, it correctly match the patterns double quoted and shown as follows:

{Engine._convert_patterns_to_prompt(correct_patterns[i])}

However, it mistakenly match the patterns double quoted and shown as follows:

{Engine._convert_patterns_to_prompt(incorrect_patterns[i])}

""", range(cnt)))
        ans = self._chain.fix_regex.run(
            facts=f"""
{fact_0_str}

{regex_list_str}

Now, I will provide to you the other {cnt} facts.

{facts}
        """
        )
        if ans.endswith('""'):
            ans = ans[:-1]
        try:
            parsed_result = list(map(eval, ans.strip().split('\n')))
        except SyntaxError as e:
            raise ValueError(ans) from e

        assert len(regex_list) == len(parsed_result)
        for regex, result in zip(regex_list, parsed_result):
            try:
                assert regex == result[0], f'original regex is changed: {regex[0]}!={regex}'
                assert re.compile(result[1]), f'{result[1]} cannot be compiled'
            except BaseException as e:
                raise ValueError(f'Parsing result {result} failed') from e
        try:
            result = list(map(lambda x: x[1], parsed_result))
        except IndexError as e:
            raise ValueError(parsed_result) from e
        return result[0]
