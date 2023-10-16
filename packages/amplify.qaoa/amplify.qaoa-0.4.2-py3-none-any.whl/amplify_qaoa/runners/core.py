from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, Union
import itertools
from collections import Counter, defaultdict

CoeffType = Union[Tuple[()], Tuple[int, ...]]
IsingDict = Dict[CoeffType, float]


def get_nqubit(f_dict: IsingDict, group_list: List[List[int]]) -> int:
    index_set = set()
    for key in f_dict.keys():
        index_set |= set(key)
    index_set |= set(itertools.chain.from_iterable(group_list))
    return max(index_set) + 1


def decode_solutions(raw_solution: Dict[str, int]) -> List[Tuple[List[int], int]]:
    return [
        (
            [-1 if int(i) > 0 else 1 for i in reversed(assignments)],
            frequency,
        )
        for (assignments, frequency) in raw_solution.items()
    ]


def reduce_degree(f_dict: IsingDict) -> IsingDict:
    reduced_f_dict = defaultdict(float)

    for key, value in f_dict.items():
        count = Counter(key)
        reduced_key = tuple(i for i, a in count.items() if a % 2 == 1)
        reduced_f_dict[reduced_key] += value

    return reduced_f_dict


class AbstractQAOARunner(metaclass=ABCMeta):
    _shots: Optional[int]
    _f_dict: Optional[IsingDict]
    _wires: Optional[int]
    _opt_params: Optional[List[float]]
    _group_list: Optional[List[List[int]]]
    _init_ones: Optional[List[int]]

    @property
    def shots(self):
        return self._shots

    @shots.setter
    def shots(self, value):
        self._shots = value

    def __init__(
        self,
        reps: int = 10,
        shots: Optional[int] = None,
    ) -> None:
        super().__init__()
        self.reps = reps
        self.shots = shots

        self._f_dict = None
        self._wires = None
        self._opt_params = None
        self._group_list = None
        self._init_ones = None

    @property
    def wires(self):
        return self._wires

    @property
    def opt_params(self):
        return self._opt_params

    @abstractmethod
    def tune(
        self,
        f_dict: IsingDict,
        wires: int,
        optimizer: str,
        group_list: List[List[int]],
        init_ones: List[int],
        initial_parameters: Optional[List[float]] = None,
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def measure(
        self,
        f_dict: IsingDict,
        wires: int,
        parameters: List[float],
        group_list: List[List[int]],
        init_ones: List[int],
    ) -> Tuple[Dict[str, int], Dict[str, float]]:
        pass

    def run(
        self,
        f_dict: Optional[IsingDict] = None,
        wires: Optional[int] = None,
        parameters: Optional[List[float]] = None,
        group_list: Optional[List[List[int]]] = None,
        init_ones: Optional[List[int]] = None,
    ) -> Tuple[List[Tuple[List[int], int]], Dict[str, float]]:
        time_taken = {}

        if f_dict is not None:
            if group_list is None:
                group_list = []
            if init_ones is None:
                init_ones = []
            if wires is None:
                wires = get_nqubit(f_dict, group_list)
            if parameters is None:
                result = self.tune(
                    f_dict=f_dict,
                    wires=wires,
                    optimizer="COBYLA",
                    group_list=group_list,
                    init_ones=init_ones,
                )
                parameters = result["opt_params"]
                time_taken = result["tune_time_taken"]
        elif self._f_dict is not None:
            f_dict = self._f_dict
            wires = self._wires
            parameters = self._opt_params
            group_list = self._group_list
            init_ones = self._init_ones
        else:
            raise RuntimeError("Problem was not specified.")

        if wires is None:
            raise RuntimeError("wires was not specified.")
        if parameters is None:
            raise RuntimeError("parameters was not specified.")
        if group_list is None:
            raise RuntimeError("group_list was not specified.")
        if init_ones is None:
            raise RuntimeError("init_ones was not specified.")

        counts, measure_time_taken = self.measure(
            f_dict,
            wires,
            parameters,
            group_list,
            init_ones,
        )

        return decode_solutions(counts), dict(**time_taken, **measure_time_taken)
