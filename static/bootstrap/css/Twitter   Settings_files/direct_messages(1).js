"use strict";provide(function(A){using("core/jquery","core/clock","app/data/direct_messages","app/ui/direct_message_dialog",function(F,E,D,C){function B(H){D.attachTo(document,H);C.attachTo("#dm_dialog",H);E.setIntervalEvent("uiNeedsDMConversations",90*1000)}var G=!!F("#dm_dialog").length;A(G?B:F.noop)})});