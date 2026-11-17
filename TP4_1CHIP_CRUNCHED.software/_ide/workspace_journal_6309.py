# 2026-09-01T10:34:37.146874012
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

platform = client.get_component(name="platform")
status = platform.build()

comp = client.get_component(name="TP4_service")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../TP4_1CHIP_CRUNCHED.hw_export/design_1_wrapper_02.xsa")

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

vitis.dispose()

