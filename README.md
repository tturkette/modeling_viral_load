[![Python application test with Github Actions](https://github.com/tturkette/modeling_viral_load/actions/workflows/main.yml/badge.svg)](https://github.com/tturkette/modeling_viral_load/actions/workflows/main.yml)

# Overview:

There are many methods to model viral load after treatment with a drug. One of these is using the bi-directional decay equation:

$$ V(t) = A \cdot \mathrm{exp}(-\alpha t) + B \cdot \mathrm{exp}(-\beta t) $$

This script utilizes the scipy package to fit the parameters based on viral load data obtained from HIV patients following treatment using a non-linear least squares method.
