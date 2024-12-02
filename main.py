def introspection_info(obj):
    info = {}

    # Тип объекта
    info['Type'] = type(obj).__name__

    # Атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['Attributes'] = attributes

    # Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['Methods'] = methods

    # Модуль, к которому объект принадлежит
    info['Module'] = getattr(obj, '__module__', 'N/A')

    # Дополнительные свойства
    if hasattr(obj, '__dict__'):
        info['Additional Properties'] = obj.__dict__

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)

class Example:
    def __init__(self):
        self.attr1 = 'value1'
        self.attr2 = 'value2'

    def method1(self):
        pass

    def method2(self):
        pass

example_info = introspection_info(Example())
print(example_info)
