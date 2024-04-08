if [ -d data/vocab ]
then
 echo "vocab dir already exists"
else
  mkdir "./data/vocab"
fi
if [ -d data/dataset ]
then
  echo "dataset dir already exists"
else
 mkdir "./data/dataset"
fi
if [ -d data/result ]
then
  echo "result dir already exists"
else
 mkdir "./data/result"
fi
wget https://github.com/stella-cv/FBoW_orb_vocab/raw/main/orb_vocab.fbow -O ./data/vocab/orb_vocab.fbow

if [[ -d openvslam-1 ]]
then
  echo "openvslam-1 already cloned"
else
  git clone --recursive https://github.com/Gizzatovamir/openvslam-1.git
fi

docker build -t stella_vslam-desktop -f openvslam-1/Dockerfile.desktop .