n=1;
max=25;
while [ "$n" -le "$max" ]; do
  mkdir "Day $n"
  n=`expr "$n" + 1`;
done