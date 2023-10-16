from pathlib import Path
import pytest

from hpcflow.app import app as hf
from hpcflow.sdk.core.errors import MissingActionEnvironment


@pytest.fixture
def dummy_action_kwargs_pre_proc():
    act_kwargs = {
        "commands": [hf.Command("ls")],
        "input_file_generators": [
            hf.InputFileGenerator(
                input_file=hf.FileSpec("inp_file", name="file.inp"),
                inputs=[hf.Parameter("p1")],
            )
        ],
    }
    return act_kwargs


def test_action_equality(null_config):
    a1 = hf.Action(commands=[hf.Command("ls")], environments=[])
    a2 = hf.Action(commands=[hf.Command("ls")], environments=[])
    assert a1 == a2


def test_action_scope_to_string_any():
    assert hf.ActionScope.any().to_string() == "any"


def test_action_scope_to_string_main():
    assert hf.ActionScope.main().to_string() == "main"


def test_action_scope_to_string_processing():
    assert hf.ActionScope.processing().to_string() == "processing"


def test_action_scope_to_string_input_file_generator_no_kwargs():
    assert hf.ActionScope.input_file_generator().to_string() == "input_file_generator"


def test_action_scope_to_string_output_file_parser_no_kwargs():
    assert hf.ActionScope.output_file_parser().to_string() == "output_file_parser"


def test_action_scope_to_string_input_file_generator_with_kwargs():
    assert (
        hf.ActionScope.input_file_generator(file="file1").to_string()
        == "input_file_generator[file=file1]"
    )


def test_action_scope_to_string_output_file_parser_with_kwargs():
    assert (
        hf.ActionScope.output_file_parser(output="out1").to_string()
        == "output_file_parser[output=out1]"
    )


def test_action_scope_class_method_init_scope_any():
    assert hf.ActionScope(typ=hf.ActionScopeType.ANY) == hf.ActionScope.any()


def test_action_scope_class_method_init_scope_main():
    assert hf.ActionScope(typ=hf.ActionScopeType.MAIN) == hf.ActionScope.main()


def test_action_scope_class_method_init_scope_processing():
    assert (
        hf.ActionScope(typ=hf.ActionScopeType.PROCESSING) == hf.ActionScope.processing()
    )


def test_action_scope_class_method_init_scope_input_file_generator_no_kwargs():
    assert (
        hf.ActionScope(typ=hf.ActionScopeType.INPUT_FILE_GENERATOR)
        == hf.ActionScope.input_file_generator()
    )


def test_action_scope_class_method_init_scope_output_file_parser_no_kwargs():
    assert (
        hf.ActionScope(typ=hf.ActionScopeType.OUTPUT_FILE_PARSER)
        == hf.ActionScope.output_file_parser()
    )


def test_action_scope_class_method_init_scope_input_file_generator_with_kwargs():
    assert hf.ActionScope(
        typ=hf.ActionScopeType.INPUT_FILE_GENERATOR, file="file1"
    ) == hf.ActionScope.input_file_generator(file="file1")


def test_action_scope_class_method_init_scope_output_file_parser_with_kwargs():
    assert hf.ActionScope(
        typ=hf.ActionScopeType.OUTPUT_FILE_PARSER, output="out1"
    ) == hf.ActionScope.output_file_parser(output="out1")


def test_action_scope_raise_on_unknown_kwargs_type_any():
    with pytest.raises(TypeError):
        hf.ActionScope(typ=hf.ActionScopeType.ANY, bad="arg")


def test_action_scope_raise_on_unknown_kwargs_type_main():
    with pytest.raises(TypeError):
        hf.ActionScope(typ=hf.ActionScopeType.MAIN, bad="arg")


def test_action_scope_raise_on_unknown_kwargs_type_processing():
    with pytest.raises(TypeError):
        hf.ActionScope(typ=hf.ActionScopeType.PROCESSING, bad="arg")


def test_action_scope_raise_on_unknown_kwargs_type_input_file_generator():
    with pytest.raises(TypeError):
        hf.ActionScope(typ=hf.ActionScopeType.INPUT_FILE_GENERATOR, bad="arg")


def test_action_scope_raise_on_unknown_kwargs_type_output_file_parser():
    with pytest.raises(TypeError):
        hf.ActionScope(typ=hf.ActionScopeType.OUTPUT_FILE_PARSER, bad="arg")


def test_action_scope_no_raise_on_good_kwargs_type_input_file_generator():
    hf.ActionScope(typ=hf.ActionScopeType.INPUT_FILE_GENERATOR, file="file1")


def test_action_scope_no_raise_on_good_kwargs_type_output_file_parser():
    hf.ActionScope(typ=hf.ActionScopeType.OUTPUT_FILE_PARSER, output="out1")


def test_action_scope_no_raise_on_no_kwargs_type_input_file_generator():
    hf.ActionScope(typ=hf.ActionScopeType.INPUT_FILE_GENERATOR)


def test_action_scope_no_raise_on_no_kwargs_type_output_file_parser():
    hf.ActionScope(typ=hf.ActionScopeType.OUTPUT_FILE_PARSER)


def test_action_scope_json_like_round_trip():
    as1 = hf.ActionScope.input_file_generator(file="file1")
    js, _ = as1.to_json_like()
    as1_rl = hf.ActionScope.from_json_like(js)
    assert as1 == as1_rl


def test_action_scope_from_json_like_string_and_dict_equality():
    as1_js = "input_file_generator[file=file1]"
    as2_js = {
        "type": "input_file_generator",
        "kwargs": {
            "file": "file1",
        },
    }
    assert hf.ActionScope.from_json_like(as1_js) == hf.ActionScope.from_json_like(as2_js)


def test_get_command_input_types_sub_parameters_true_no_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1>> + 100)")])
    assert act.get_command_input_types(sub_parameters=True) == ("p1",)


def test_get_command_input_types_sub_parameters_true_with_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1.a>> + 100)")])
    assert act.get_command_input_types(sub_parameters=True) == ("p1.a",)


def test_get_command_input_types_sub_parameters_false_no_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1>> + 100)")])
    assert act.get_command_input_types(sub_parameters=False) == ("p1",)


def test_get_command_input_types_sub_parameters_false_with_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1.a>> + 100)")])
    assert act.get_command_input_types(sub_parameters=False) == ("p1",)


def test_get_command_input_types_sum_sub_parameters_true_no_sub_param():
    act = hf.Action(commands=[hf.Command("Write-Output <<sum(parameter:p1)>>")])
    assert act.get_command_input_types(sub_parameters=True) == ("p1",)


def test_get_command_input_types_sum_sub_parameters_true_with_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output <<sum(parameter:p1.a)>>")])
    assert act.get_command_input_types(sub_parameters=True) == ("p1.a",)


def test_get_command_input_types_sum_sub_parameters_false_no_sub_param():
    act = hf.Action(commands=[hf.Command("Write-Output <<sum(parameter:p1)>>")])
    assert act.get_command_input_types(sub_parameters=False) == ("p1",)


def test_get_command_input_types_sum_sub_parameters_false_with_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output <<sum(parameter:p1.a)>>")])
    assert act.get_command_input_types(sub_parameters=False) == ("p1",)


def test_get_command_input_types_label_sub_parameters_true_no_sub_param():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1[one]>> + 100)")])
    assert act.get_command_input_types(sub_parameters=True) == ("p1[one]",)


def test_get_command_input_types_label_sub_parameters_true_with_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1[one].a>> + 100)")])
    assert act.get_command_input_types(sub_parameters=True) == ("p1[one].a",)


def test_get_command_input_types_label_sub_parameters_false_no_sub_param():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1[one]>> + 100)")])
    assert act.get_command_input_types(sub_parameters=False) == ("p1[one]",)


def test_get_command_input_types_label_sub_parameters_false_with_sub_parameter():
    act = hf.Action(commands=[hf.Command("Write-Output (<<parameter:p1[one].a>> + 100)")])
    assert act.get_command_input_types(sub_parameters=False) == ("p1[one]",)


def test_get_script_name(null_config):
    expected = {
        "<<script:/software/hello.py>>": "hello.py",
        "<<script:software/hello.py>>": "hello.py",
        r"<<script:C:\long\path\to\script.py>>": "script.py",
        "/path/to/script.py": "/path/to/script.py",
    }
    for k, v in expected.items():
        assert hf.Action.get_script_name(k) == v


def test_is_snippet_script(null_config):
    expected = {
        "<<script:/software/hello.py>>": True,
        "<<script:software/hello.py>>": True,
        r"<<script:C:\long\path\to\script.py>>": True,
        "/path/to/script.py": False,
    }
    for k, v in expected.items():
        assert hf.Action.is_snippet_script(k) == v


def test_get_snippet_script_path(null_config):
    expected = {
        "<<script:/software/hello.py>>": Path("/software/hello.py"),
        "<<script:software/hello.py>>": Path("software/hello.py"),
        r"<<script:C:\long\path\to\script.py>>": Path(r"C:\long\path\to\script.py"),
    }
    for k, v in expected.items():
        assert hf.Action.get_snippet_script_path(k) == v


def test_get_snippet_script_path_False(null_config):
    assert not hf.Action.get_snippet_script_path("/path/to/script.py")
