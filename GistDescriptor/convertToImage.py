import numpy,scipy, os, array, scipy.misc, sys
def convertToImage(dirPath, filename):
   try: 
      f = open(dirPath + filename,'rb');
      ln = os.path.getsize(dirPath + filename); # length of file in bytes
      width = 256;
      rem = ln%width; 

      a = array.array("B"); # uint8 array
      a.fromfile(f,ln-rem);
      f.close(); 

      g = numpy.reshape(a,(len(a)/width,width));
      g = numpy.uint8(g);
      #out = filename + '.png';
      # print 'Output filename:' + out;
      scipy.misc.imsave(dirPath + filename + '.png', g); # save the image
   except Exception: 
      print 'Error when process ' + filename;
      pass;

if __name__ == '__main__':
   print 'Directory:' + sys.argv[1];
   dirPath = sys.argv[1];
   for filename in os.listdir(dirPath):
      convertToImage(dirPath, filename);
   print 'Finished !';
