#!/bin/bash

folder=/home/ubuntu/Desktop/PIKIT-5_WORKING/DVRJetson
input=$folder/supporting_scripts/rtsp.txt

scr=0
while IFS= read -r line
do
a=''
i=0
for word in $(echo $line | sed -n 1'p' | tr ',' '\n')
do
var[$i]=$word
i=$((i+1))
done
scr=$((scr+1))
file=$folder/DVRscripts/script$scr.sh
if [ -f $file ]; then
rm $file
fi
rm -rf "$folder/DVR/${var[1]}/"
sudo mkdir "$folder/DVR/${var[1]}"
echo "#!/bin/bash" >> $file
echo "while true" >> $file
echo "do" >> $file
OUT="$folder/DVR/${var[1]}/%s.mp4"
INP="${var[0]}"
echo "    "sudo ffmpeg -i "\"${INP}\"" -c "copy"  -map 0 -f segment -segment_time 600 -strftime 1 "\"${OUT}\""  >>$file
echo "    "sudo chmod -R 777 "*" >>$file
echo "done" >> $file
echo "Written to $file"
echo ""
done < "$input"
echo ""
echo "**********"
echo "Changing Owner Permissions"
echo "**********"
echo ""

cd && cd "$folder/"
sudo chown -R ubuntu *




