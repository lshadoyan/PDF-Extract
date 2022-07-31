import course_finder as cf 
import pathway as p  

def main():
    pathway = p.pathway_msg()
    args = cf.cli()
    if args.p is not None: 
        path = str(args.p)
    else:
        print(pathway)
        path = input("Pathway Concept: ")
    path_courses = p.csv_create(path)
    course_name, gpas = cf.course_finder(path_courses)
    cf.write(course_name, gpas)
    cf.sort()
    print("Data sorted in output.csv file") 

if __name__ == "__main__": 
    main() 