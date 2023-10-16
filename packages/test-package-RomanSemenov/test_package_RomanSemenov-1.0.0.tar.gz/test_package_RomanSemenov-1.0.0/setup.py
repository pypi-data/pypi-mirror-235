from setuptools import setup

# long_description=readme(),
# long_description_content_type='text/markdown',

setup(
    name='test_package_RomanSemenov',
    version='1.0.0',
    author='RomanSemenov',
    author_email='romansemenov2109@gmail.com',
    description='This is my first module',
    long_description = """Тут длинное описание всего проекта (в данном случае мой пакет добавляет 1 к числу)""",
    packages = ["test_package_RomanSemenov"]
)