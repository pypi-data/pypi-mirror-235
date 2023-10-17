from typing import List, Optional
from pydantic import BaseModel


class UIPortGroupParams(BaseModel):
    """UI port logic for port group
    :param id_: port_group_id
    :param show_ports: show port panels
    :param can_add: can add new port to group
    :param can_delete: can delete port from group
    :param can_move: can move port inside group
    :param can_hide: can hide port
    :param can_set_type: can set porttype to port
    :param has_code: has editable code field
    :param has_special: has special binary switch
    :param has_required: has required binary switch
    :param copy_name_from_code: copy port name from code field when code edting
    :param group_title: visual title for port group
    :param special_title: title|tooltip for special
    :param code_title: title|tooltip for code
    :param copy_from_group: port group name
    :param code_validator_callback_name: name of classmethod for port code validation
        func(str: code) -> {'is_valid': bool, 'bad_symbol_indexes': list, error_string: str}
        if is_valid == False, show tooltip or toster with  error_string, and underline/colorize misspelled
        symbols with bad_symbol_indexes
    :param node_updater_callback_name: name of classmethod for updating node after editing ports in this group
        func(cfg: NodeConfig) -> cfg: NodeConfig
    :param valid_types: valid types for ports in this group
    """
    id_: str = ''  # port_group_id
    show_ports: bool = True  # show port panels
    can_add: bool = False  # can add new port to group
    can_delete: bool = False  # can add delete port from group
    can_move: bool = False  # can move port inside group
    can_hide: bool = False  # can hide port
    can_set_type: bool = False  # can set porttype to port
    has_code: bool = False  # has editable code field
    has_special: bool = False  # has special binary switch
    has_required: bool = False  # has required binary switch
    copy_name_from_code: bool = True  # copy port name from code field when code edting
    group_title: Optional[str]  # visual title for port group
    special_title: Optional[str]  # title|tooltip for special
    code_title: Optional[str]  # title|tooltip for code
    code_special_title: Optional[str]  # title|tooltip for code for pressed key
    copy_from_group: Optional[str]  # port group name
    node_updater_callback_name: Optional[str]
    code_validator_callback_name: Optional[str]
    valid_types: List[str] = []
    placeholder: Optional[str]  # input placeholder_text


class UIParams(BaseModel):
    """UI parameters for node UI port logic

    :param input_groups: list of input port groups (subgroups of inputs)
    :param output_groups: list of output port groups (subgroups of outputs)
    :param ui_config_schema: json schema of ui_config
    """
    input_groups: List[UIPortGroupParams] = [UIPortGroupParams(id_='inputs')]
    output_groups: List[UIPortGroupParams] = [UIPortGroupParams(id_='outputs')]
    ui_config_schema: str = ''


class DestructurerUIParams(UIParams):
    """Destructurer UI port logic
    """
    input_groups: List[UIPortGroupParams] = [UIPortGroupParams(id_='inputs', show_ports=False)]
    output_groups: List[UIPortGroupParams] = [
        UIPortGroupParams(
            id_='outputs',
            can_add=True,
            can_delete=True,
            can_move=True,
            has_code=True,
            can_hide=True,
            can_set_type=True,
            has_required=True,
            code_title='query',
            placeholder='entire message if empty',
        ),
        UIPortGroupParams(
            id_='data_attrs',
            can_add=False,
            can_delete=False,
            can_move=False,
            has_code=False,
            can_hide=True,
            can_set_type=False,
            has_required=False
        )
    ]


class StructurerUIParams(UIParams):
    """Structurer UI port logic
    """
    input_groups: List[UIPortGroupParams] = [UIPortGroupParams(
        id_='inputs',
        can_add=True,
        can_delete=True,
        can_move=True,
        has_code=True,
        can_hide=True,
        can_set_type=True,
        has_required=True,
        # has_special=True,
        code_title='path',
        # code_special_title='path',
        # special_title='use jspath',  # noqa: F722
        placeholder='entire message if empty',
    )]
    output_groups: List[UIPortGroupParams] = [UIPortGroupParams(id_='outputs', show_ports=False)]
