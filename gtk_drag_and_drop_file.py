import gi
gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)

box = Gtk.HBox()
window.add(box)

def on_drag_data_get(widget, drag_context, data, info, time):
    data.set_uris(["file:///home/user/test.html"])

def on_drag_data_received(widget, drag_context, x, y, data, info, time):
    print("Received text: <%s>" % bytes(data.get_text(), "utf-8"))
    print("Drag context:",
        "drag_context.get_actions(): %s\n" % drag_context.get_actions(),
        "drag_context.get_dest_window(): %s\n" % drag_context.get_dest_window(),
        "drag_context.get_device(): %s\n" % drag_context.get_device(),
        "drag_context.get_protocol(): %s\n" % drag_context.get_protocol(),
        "drag_context.list_targets(): %s\n" % drag_context.list_targets(),
    )

drag_button = Gtk.Button(label="Drag")
drag_button.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], Gdk.DragAction.COPY | Gdk.DragAction.MOVE | Gdk.DragAction.LINK | Gdk.DragAction.ASK)
drag_button.drag_source_add_text_targets()
drag_button.connect("drag-data-get", on_drag_data_get)
box.add(drag_button)

drop_button = Gtk.Button(label="Drop")
drop_button.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY | Gdk.DragAction.MOVE | Gdk.DragAction.LINK | Gdk.DragAction.ASK)
drop_button.drag_dest_add_text_targets()
drop_button.connect("drag-data-received", on_drag_data_received)
box.add(drop_button)

window.show_all()
Gtk.main()