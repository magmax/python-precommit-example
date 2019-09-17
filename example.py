from os import path
import argparse
import argparse


def   main ( ) :
   parser = argparse.ArgumentParser(description = 'Example for pre-commit.')
   parser.add_argument('integers' , metavar = 'N' , type=int, nargs='+' ,
                    help  ='an integer for the accumulator')

   args  = parser.parse_args ()
   total = sum(args.integers)  #sum all integers
   current_dir = path.abspath ( path.curdir )

   print (f"Running from path {current_dir}"  )
   print ( f"Arguments are: {args.integers}"
   )
   print (
    f"Total: {total}"
   )



main (  )

# update this line and try to commit
