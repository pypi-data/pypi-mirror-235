from smi_python_commons.arguments.argument import Argument

from smi_python_tbi_parser.tbi import parse_tbi

SMI_TBI_FILE_ARGUMENT = Argument('smi-tbi-file', 't', parse_tbi, 'TBI yaml to be used', True)
