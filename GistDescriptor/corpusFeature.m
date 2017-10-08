% Load image from the directory
myDir = 'Image'; %gets directory
myFiles = dir(fullfile(myDir,'*.png')); %gets all png files in struct
features = [];
numError = 0;
numFile = 0;
num = 100; % Export the results after processing 300 files.
for k = 1:length(myFiles)
  numFile ++;
  baseFileName = myFiles(k).name;
  fullFileName = fullfile(myDir, baseFileName);
  % fprintf(1, 'No %d reading %s\n', numFile, fullFileName);
  try
    feature = computeGist(fullFileName); 
    features = [features; feature];
    
    if (numFile > num)
      fprintf(1, 'Output the result %d\n', numFile); 
      csvwrite('corpusFeatures.csv', features);
      num += num;
    endif  
  catch
    fprintf(1, 'Error %s\n', fullFileName); 
    numError ++; 
  end_try_catch
  
  %[wavData, Fs] = wavread(fullFileName);
  % all of your actions for filtering and plotting go here
end

% Save feature (matrix) to file
fprintf(1, 'Number of errors %d\n', numError); 
csvwrite('corpusFeatures.csv', features);


