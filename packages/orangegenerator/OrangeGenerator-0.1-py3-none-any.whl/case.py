from pathlib import Path
import subprocess
from typing import Callable, TextIO


class TestGenertor:
    """
    测试用例生成器
    """
    def __init__(self, path: Path, program: str = "std") -> None:
        self.file_names: list[int] = []
        self.test_cases: list[tuple[Callable[[TextIO], None], int]] = []
        self.program: str = program
        self.path = path
        
    def compile_program(self, *args: list[tuple[str,str]]) -> None:
        """编译程序

        Args:
            program (str, optional): 待编译的程序. Defaults to "std".
        """
        compile_cmd = f"g++ {self.program}.cpp -o {self.program}.exe"
        for arg, value in args:
            compile_cmd += f" -{arg} {value}"
        subprocess.run(compile_cmd, shell=True)

    def add(self, id: int | None = None, case: Callable[[TextIO], None] | None = None) -> None:
        """增加测试用例

        Args:
            id (int): 测试用例的编号
            case (Callable[[TextIO], None] | None, optional): 生成用例的函数. Defaults to None.
        """
        if id is None:
            id = len(self.file_names) + 1
        if case is not None:
            self.test_cases.append((case, id))
        self.file_names.append(id)

    def gen_all_case(self):
        """
        生成所有测试用例
        """
        for case, id in self.test_cases:
            with open(self.path / f"{id}.in", "w", encoding="utf-8") as f:
                case(f)

    def gen_answer(self, case_id: int, program: str = "std"):
        """生成答案

        Args:
            case_id (int): 测试用例的编号
            program (str, optional): 标准程序. Defaults to "std.exe".
        """
        in_file = open(self.path / f"{case_id}.in", "r", encoding="utf-8")
        out_file = open(self.path / f"{case_id}.out", "w", encoding="utf-8")
        subprocess.run(f"{self.program}.exe", stdin=in_file, stdout=out_file, timeout=1)
        #         compile_cmd = f"g++ {program}.cpp -o {program}.exe"
        # subprocess.run(compile_cmd, shell=True)
        out_file.close()
        in_file.close()

    def gen_all(self):
        self.gen_all_case()
        self.compile_program()
        for id in self.file_names:
            self.gen_answer(id)



# def test_case1(f: TextIO):
#     n: int = int(2e5)
#     k: int = random.randint(n // 5, n - 1)
#     s: int = random.randint(n // 2, n - 1)

#     print(f"{n} {k} {s}", file=f)
#     for _ in range(n + 1):
#         print(f"{random.randint(1,5)} {random.randint(1,100000)}", file=f)


# def test_case2(f: TextIO):
#     n: int = int(2e5)
#     k: int = randodd(1, 5)
#     s: int = randodd(n // 2, n - 1)

#     print(f"{n} {k} {s}", file=f)
#     for _ in range(n + 1):
#         print(f"{randodd(1,10000)} {randodd(1,100000)}", file=f)
        
# def test_case3(f: TextIO):
#     n: int = int(2e5)
#     k: int = randodd(1, n // 30)
#     s: int = randodd(n // 2, n - 1)

#     print(f"{n} {k} {s}", file=f)
#     for _ in range(n + 1):
#         print(f"{randodd(1,10000)} {randodd(1,100000)}", file=f)
        

# def test_case4(f: TextIO):
#     n: int = int(1e5)
#     k: int = 1
#     s: int = randodd(n // 2, n - 1)
#     print(f"{n} {k} {s}", file=f)
#     for _ in range(n + 1):
#         print(f"{1} {randint(1,100000)}", file=f)
        
# def test_case5(f: TextIO):
#     n: int = int(2e5)
#     k: int = 1
#     s: int = n
    
#     print(f"{n} {k} {s}", file=f)
#     for _ in range(n + 1):
#         print(f"{randint(1,1)} {randint(1,100000)}", file=f)
    
    
# test = TestGenertor()
# test.add(id = 1)
# test.add(case = test_case1)
# test.add(case = test_case2)
# test.add(case = test_case3)
# test.add(case = test_case4)
# test.add(case = test_case5)
# test.add(case = test_case3)
# test.add(case = test_case3)
# test.add(case = test_case3)
# test.add(case = test_case3)
# test.gen_all()

