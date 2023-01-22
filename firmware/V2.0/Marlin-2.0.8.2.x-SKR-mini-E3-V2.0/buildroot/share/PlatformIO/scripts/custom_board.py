#
# buildroot/share/PlatformIO/scripts/custom_board.py
#
import marlin
board = marlin.env.BoardConfig()

if address := board.get("build.address", ""):
	marlin.relocate_firmware(address)

if ldscript := board.get("build.ldscript", ""):
	marlin.custom_ld_script(ldscript)
