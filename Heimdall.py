from argparse import ArgumentParser
from src.gui.main import GUI
from plugins._lib.Data import getDatapointbyString
import sys

class helpOnDefaultParser(ArgumentParser):
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
    myCore.search(datapoint=getDatapointbyString(args.datapoint),keyword=args.keyword)
    # Process Data here
    
if __name__ == "__main__":
    parser = helpOnDefaultParser(
        prog="Heimdall",
        description="The (soon™ to be) best open source all in one modular osint search engine")
    # either gui or list datapoints or search in cli mode
    guiORdirectInput = parser.add_mutually_exclusive_group()
    guiORdirectInput.add_argument("-g","--gui",action="store_true",help="start the heimdall gui",default=False)
    guiORdirectInput.add_argument("-k","--keyword",help="search input",type=str)
    guiORdirectInput.add_argument("-l","--list",action="store_true",help="list of available datapoints",default=False)
    parser.add_argument("-dp","--datapoint",help="define keyword datatype (--listDatapoints for a list)",type=str)
    parser.add_argument("-D","--debug",action="store_true",help="enable debug logging",default=False)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    start()