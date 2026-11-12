import argparse,csv,json,sys
def transform(rows):
    return [r for r in rows if any(str(v).strip() for v in r.values())]

def main():
    parser=argparse.ArgumentParser(description='CSV empty row pruner')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    reader=csv.DictReader(source.splitlines())
    result=transform(list(reader))
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
