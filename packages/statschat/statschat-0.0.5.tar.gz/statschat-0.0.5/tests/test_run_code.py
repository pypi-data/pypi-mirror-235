import codecs
import re
import subprocess

from statschat.stats_chat import StatsCHAT
import unittest


class TestCases(unittest.IsolatedAsyncioTestCase):
    async def testRunCode(self):
        # code = 'python\nprint(\"Hello, World!\")\n'  # 你得到的代码字符串
        code = '''import pandas as pd\nimport matplotlib.pyplot as plt\n\n# Read the dataset\ndf = pd.read_excel('./input/dt.xlsx')\n\n# Plot the age distribution\nplt.hist(df['age'], bins=10, edgecolor='black')\nplt.xlabel('Age')\nplt.ylabel('Frequency')\nplt.title('Age Distribution')\nplt.savefig('./output/age_distribution.png')\nprint('Age distribution plot saved as age_distribution.png')'''  # 你得到的代码字符串
        # 解码字符串中的转义字符和换行符
        # decoded_code, _ = codecs.escape_decode(code.encode('utf-8'))
        # 去掉换行符和转义字符
        # code = code.replace('\n', '').replace('\\"', '"')
        # if code.startswith('python'):
        #     code = code[len('python'):]

        result = subprocess.run(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            err_message = result.stderr
            print(err_message)
        else:
            output = result.stdout
            print(output)


if __name__ == "__main__":
    unittest.main()
