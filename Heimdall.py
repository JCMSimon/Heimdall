from argparse import ArgumentParser
import sys

class helpOnDefaultParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def start():
    if args.gui:
        from src.gui.gui import GUI
        HeimdallUI = GUI(DEBUG=args.debug)
        return
    from src.Core import Core
    myCore = Core(DEBUG=args.debug)
    if args.list:
        print(sorted([datapoint.lower().replace(" ","") for datapoint in myCore.pluginRegister.getAvailableDatapoints()]))
        return
    # no gui and no listing of datapoint -> keyword is needed
    if args.keyword is None:
        return
    if args.keyword.strip() == "":
        print("Heimdall: error: argument -k/--keyword: can not be an empty string")
        return
    if args.datapoint is None:
        print("Heimdall: error: argument -dp/--datapoint is required if -k/--keyword is used")
        return
    if args.datapoint.strip() == "":
        print(f"Heimdall: error: argument -dp/--datapoint: can not be an empty string")
        return
    if args.datapoint.strip().lower().replace(" ","") not in [datapoint.lower().replace(" ","") for datapoint in myCore.pluginRegister.getAvailableDatapoints()]:
        print(f"Heimdall: error: None of your plugins support the datatype: '{args.datapoint}'")
        return
    # Finally everything is validated and we can perform the search pog
    from src.plugin.Data import getDatapointbyString
    myCore.search(datapoint=getDatapointbyString(args.datapoint),keyword=args.keyword)
    todo = [myCore.rootNode]
    print("--- RESULTS ---") #TODO | This is a makeshift solution for now.
    for node in todo:
        todo.extend(node._children)
        # Filter out root node (ik this is dirty sorry)
        if "dp._internal.is_root_node" in node.datapoints[0]: 
            continue
        print(f"> {node.title}")
        for dp in node.datapoints:
            for key,value in dp.items():
                print(f"-> {value}")
        
        
        
    
if __name__ == "__main__":
    parser = helpOnDefaultParser(
        prog="Heimdall",
        description="The (soon™ to be) best open source all in one modular osint search engine")
    # either gui or list datapoints or search in cli mode
    guiORdirectInputORListdp = parser.add_mutually_exclusive_group()
    guiORdirectInputORListdp.add_argument("-g","--gui",action="store_true",help="start the heimdall gui",default=False)
    guiORdirectInputORListdp.add_argument("-k","--keyword",help="search input",type=str)
    guiORdirectInputORListdp.add_argument("-l","--list",action="store_true",help="list of available datapoints",default=False)
    # guiORdirectInputORListdp.add_argument("-le","--listExports",action="store_true",help="list of available datapoints",default=False)
    parser.add_argument("-dp","--datapoint",help="define keyword datatype (--listDatapoints for a list)",type=str)
    parser.add_argument("-D","--debug",action="store_true",help="enable debug logging",default=False)
    # parser.add_argument("-e","--export",help="export file type",type=str)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    start()