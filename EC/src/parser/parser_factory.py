from abc import ABC, abstractmethod

from PythonPractice.EC.src.parser.parser_json import JsonParser
from PythonPractice.EC.src.parser.parser_xml import XmlParser


class AbstractParserFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_parser():
        pass


class JsonParserFactory(AbstractParserFactory):
    @staticmethod
    def create_parser():
        return JsonParser()


class XmlParserFactory(AbstractParserFactory):
    @staticmethod
    def create_parser():
        return XmlParser()


class ParserFactory:
    @staticmethod
    def parse(factory):
        parser = factory.create_parser()
        parser.parse([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


ParserFactory.parse(JsonParserFactory)
ParserFactory.parse(XmlParserFactory)

'''
Abstract Factory와 Strategy 패턴은 모두 디자인 패턴 중 하나로, 객체지향 프로그래밍에서 일반적으로 사용되는 구조입니다. 두 패턴은 서로 다른 문제를 해결하도록 설계되었습니다.

Abstract Factory 패턴은 관련된 또는 의존적인 객체들의 그룹을 생성하기 위한 인터페이스를 제공합니다.
이 패턴은 다양한 구현체를 캡슐화하고, 이들을 상황에 따라 대체할 수 있도록 합니다.
이 패턴의 주요 장점은 클라이언트 코드가 특정 구현체에 직접적으로 의존하지 않게 하여 유지보수성과 코드 재사용성을 향상시키는 것입니다.
하지만, 추상 팩토리 패턴은 각 팩토리가 생성해야 하는 제품군이 추가되거나 변경될 경우 코드를 수정해야 하는 단점이 있습니다.

Strategy 패턴은 알고리즘을 정의하고 각각을 캡슐화하여 상호 교환 가능하게 합니다.
이 패턴은 알고리즘을 사용하는 클라이언트와 독립적으로 알고리즘을 변경할 수 있도록 합니다.
이 패턴의 주요 장점은 알고리즘의 사용과 구현을 분리함으로써 코드의 유연성을 향상시키는 것입니다.
또한, 다양한 전략을 쉽게 교체하거나 확장할 수 있습니다. 그러나 Strategy 패턴을 사용하면 많은 수의 관련 클래스가 생성되며, 클라이언트가 각 전략에 대해 알아야 하는 경우도 있습니다.

따라서, 어떤 패턴을 사용할지는 개발하려는 애플리케이션의 요구 사항과 문제에 따라 달라집니다.
'''
