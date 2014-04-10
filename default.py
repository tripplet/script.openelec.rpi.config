############################################################################
#
#  Copyright 2013 Lee Smith
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################

import xbmcgui, xbmcaddon

import utils

utils.log("Started script")
if utils.get_arch() == 'RPi.arm':
    with utils.busy():
        if not utils.service_running():
            utils.start_service()

        try:
            utils.maybe_init_settings()
        except IOError as e:
            utils.read_error(utils.CONFIG_PATH, str(e))
    utils.log("Opening settings")
    xbmcaddon.Addon().openSettings()
else:
    utils.log("Not a Raspberry Pi")
    xbmcgui.Dialog().ok(utils.ADDON_NAME,
                        "This add-on only works on a Raspberry Pi")





