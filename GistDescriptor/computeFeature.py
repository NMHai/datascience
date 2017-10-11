import sys, Image,leargist

def computeFeature(filename):
   im = Image.open(filename);
   im1 = im.resize((64,64)); # for faster computation
   des = leargist.color_gist(im1); # 960 values
   feature = des[0:320]; # since the image is grayscale, we need only first 320 values

if __name__ == '__main__':
   print 'Filename:' + sys.argv[1];
   filename = sys.argv[1]; 

   computeFeature(filename);
   print 'Finished !';
 

