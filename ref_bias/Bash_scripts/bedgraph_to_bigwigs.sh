#!/bin/bash

for chrom in {1..22} X; do
    bedGraphToBigWig chr"${chrom}"_VC_dump.bedgraph hg38.chrom.sizes chr"${chrom}"_VC_dump.bw
done