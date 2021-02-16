# Write your code here
def format_time(h,m,s):
   h = str(h).rjust(2,'0') 
   m = str(m).rjust(2,'0')
   s = str(s).rjust(2,'0')

   return f'{h}:{m}:{s}'
   #return h + ":" + m + ":" + s