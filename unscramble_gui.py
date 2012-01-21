#!/usr/bin/python
'''
unscramble_gui.py - This is the gui version of unscramble.py

@author: Jason Dsouza
'''

import gtk, sys
import unscramble

__author__ = ('jasonrdsouza (Jason Dsouza)')


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        
        # Make the dictionary Trie
        self.dict_trie = unscramble.makeTrie()
        
        # Initially set full word results to false
        self.full = False
        
        # Setup the window
        self.set_title("Unscramble")
        self.set_size_request(250, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        
        # Add an icon to the program
        try:
            self.set_icon_from_file("spellcheck.png")
        except Exception, e:
            print e.message
            sys.exit(1)
        
        # Necessary to exit the program when the window is closed
        self.connect("destroy", gtk.main_quit)
        
        # Setup the layout
        vbox = gtk.VBox(False, 3)
        
        full_chk = gtk.CheckButton("Use all letters")
        entry = gtk.Entry()
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)
        vbox.pack_start(entry, False, False, 0)
        vbox.pack_start(full_chk, False, False, 0)
        
        # Setup entry capture
        entry.connect("key-release-event", self.on_key_release)
        
        # Setup checkbox capture
        full_chk.connect("clicked", self.on_clicked)
        
        # Initialize the listview
        self.store = self.create_model()
        
        treeView = gtk.TreeView(self.store)
        treeView.connect("row-activated", self.on_activated)
        treeView.set_rules_hint(True)
        sw.add(treeView)
        
        self.create_columns(treeView)
        
        # Create the statusbar
        self.statusbar = gtk.Statusbar()
        vbox.pack_start(self.statusbar, False, False, 0)
        
        # Add the vbox to the window
        self.add(vbox)
        
        # Add tooltips
        full_chk.set_tooltip_text("Force the program to only return words that use all the given letters")
        entry.set_tooltip_text("Enter scrambled letters here")
        
        # Show all the widgets on the window
        self.show_all()
    
    def create_model(self):
        store = gtk.ListStore(str)
        return store
        
    def create_columns(self, treeView):
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Unscrambled Words", rendererText, text=0)
        column.set_sort_column_id(0)
        treeView.append_column(column)
    
    def on_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        self.statusbar.push(0, text)

    def on_key_release(self, widget, event):
        self.store.clear()
        letter_combinations = unscramble.combinations(widget.get_text())
        unscrambled_list = unscramble.checkWords(self.dict_trie, letter_combinations, self.full)
        result_list = unscramble.sortListByLength(unscrambled_list)
        for word in result_list:
            self.store.append([word])
        
    def on_clicked(self, widget):
        if widget.get_active():
            self.full = True
        else:
            self.full = False
    

PyApp()
gtk.main()
