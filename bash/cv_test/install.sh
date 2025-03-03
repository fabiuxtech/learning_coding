#!/bin/bash
source ambiente.var
echo $plan
echo $clientgroup
echo $proxy1
echo $proxy2
echo $cshost
sed -e "s/\VAR_PLAN/$plan/" -e "s/\VAR_CLIENTGROUP/$clientgroup/" -e "s/\VAR_PROXY1/$proxy1/" -e "s/\VAR_PROXY2/$proxy1/" -e "s/\VAR_CSHOST/$cshost/" template.txt > new_template.txt