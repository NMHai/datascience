function feature = computeGist(filename)

% Load image (this image is not square)
% img2 = imread('demo2.jpg');
img2 = imread(filename);

% Parameters:
clear param 
%param.imageSize. If we do not specify the image size, the function LMgist
%   will use the current image size. If we specify a size, the function will
%   resize and crop the input to match the specified size. This is better when
%   trying to compute image similarities.
param.orientationsPerScale = [8 8 8 8];
param.numberBlocks = 4;
param.fc_prefilt = 4;

% Computing gist requires 1) prefilter image, 2) filter image and collect
% output energies
[gist2, param] = LMgist(img2, '', param);
feature = gist2(1:320); % since the image is grayscale, we need only first 320 values
% Visualization
%figure
%subplot(121)
%imshow(img2)
%title('Input image')
%ubplot(122)
%showGist(gist2, param)
%title('Descriptor')

% Write to new image file

