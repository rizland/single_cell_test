from bsb.morphologies import parse_morphology_file
from arborize.schematics import bsb_schematic
from arborize import neuron_build
from dbbs_models.granule_cell_models import GranuleCellModel

#modifiche al GranuleCellModel


####

# carica morfologia
morpho = parse_morphology_file('/home/martina/tool_dbbs/models/dbbs_models/morphologies/GranuleCell.swc', tags=GranuleCellModel.swc_tags)

# assembla morpho and definition file
schema = bsb_schematic(morpho, GranuleCellModel)

#craete cell
cell = neuron_build(schema)


cell.get_location((1,14)).section.psection()
cell.get_location((4,0)).section.L
