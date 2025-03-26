from domain.value_objects.prompt import Prompt, Role

p = Prompt(role=Role.USER, content="hoge")
print(p.model_dump_json())
