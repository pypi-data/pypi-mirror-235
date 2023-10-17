# vim: set expandtab shiftwidth=4 softtabstop=4:

# === UCSF ChimeraX Copyright ===
# Copyright 2022 Regents of the University of California. All rights reserved.
# This software is provided pursuant to the ChimeraX license agreement, which
# covers academic and commercial uses. For more information, see
# <http://www.rbvi.ucsf.edu/chimerax/docs/licensing.html>
#
# This file is part of the ChimeraX library. You can also redistribute and/or
# modify it under the GNU Lesser General Public License version 2.1 as
# published by the Free Software Foundation. For more details, see
# <https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>
#
# This file is distributed WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. This notice
# must be embedded in or attached to all copies, including partial copies, of
# the software or any revisions or derivations thereof.
# === UCSF ChimeraX Copyright ===

from chimerax.core.toolshed import BundleAPI

class _ZoneBundleAPI(BundleAPI):

    @staticmethod
    def initialize(session, bundle_info):
        """Install atom zone mouse mode"""
        from .zone import AtomZoneMouseMode
        zm = AtomZoneMouseMode(session)
        session._atom_zone_mouse_mode = zm	# Used by zone command
        if session.ui.is_gui:
            mm = session.ui.mouse_modes
            mm.add_mode(zm)

    @staticmethod
    def register_command(command_name, logger):
        from . import zone
        zone.register_zone_command(logger)

bundle_api = _ZoneBundleAPI()
