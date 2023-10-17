from setuptools import setup, find_packages
from pkg_resources import parse_requirements


def load_requirements(file_name: str) -> list:
    requirements = []
    with open(file_name, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name='smbh_rabbit_mq_wrapper',
    version='0.0.0.1',
    author='Alexander Vino',
    author_email='alexander-vin0@yandex.ru',
    url='https://github.com/SMEDIA-BUYING-HOLDING/RabbitMQWrapper',
    description='RabbitMQ Wrapper for solve some tasks',
    zip_safe=False,
    python_requires='>=3.10',
    packages=find_packages(),
)
