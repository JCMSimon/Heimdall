from argparse import ArgumentParser
from src.gui.main import GUI
import sys

class MyParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def start():
    if args.gui:
        HeimdallUI = GUI(DEBUG=args.debug)
        return
    from src.Core import Core
    myCore = Core(DEBUG=args.debug)
    if args.listDatapoints:
        print(myCore.pluginRegister.getAvailableDatapoints())
    if args.searchterm is None:
        return
    if args.searchterm.strip() == "":
        print("Heimdall: error: argument -st/--searchterm: can not be an empty string")
        return
    if args.datapoint is None:
        print("Heimdall: error: argument -dp/--datapoint is required if -st/--searchterm is used")
        return
    if args.datapoint.strip() == "":
        print(f"Heimdall: error: argument -dp/--datapoint: can not be an empty string")
        return
    if args.datapoint.strip().lower() not in [datapoint.lower() for datapoint in myCore.pluginRegister.getAvailableDatapoints()]:
        print(f"Heimdall: error: None of your plugins support the datatype: '{args.datapoint}'")
        return
    # Finally everything is validated and we can perform the search pog
    results = myCore.search(datapoint=args.datapoint,keyword=args.searchterm)

if __name__ == "__main__":
    parser = MyParser(prog="Heimdall",description="The best open source all in modular one osint search engine")
    guiORdirectInput = parser.add_mutually_exclusive_group()
    guiORdirectInput.add_argument("-G","--gui",action="store_true",help="start the heimdall gui",default=False) # TODO | Change default to False
    guiORdirectInput.add_argument("-st","--searchterm",help="search input",type=str)
    guiORdirectInput.add_argument("-ld","--listDatapoints",action="store_true",help="list available datapoints",default=False)
    parser.add_argument("-dp","--datapoint",help="define search term datatype (--listDatapoints for a list)",type=str)
    parser.add_argument("-D","--debug",action="store_true",help="enable debug logging",default=False)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    start()