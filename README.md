# README #
In this project, we try to provide an elegant solution for multistream classification by fusing drift detection into data shift adaptation. This is an update to the ICDE 2017 paper.

### What is this repository for? ###
* FUSION was first submitted to ICDE 2017, and then KDD 2017. 
* This is the stable version of FUSION. Download from this repository if needed. Don't use other repositories that are conference specific.
* One thing to remember, ideally number of ref points, maximum size of the window and size of the initial window should be same.

### Notes ###
* As mentioned in the readme for the repository Multistream_KLIEP_ICDE2017, there is an error in the algorithm, based on which the code-base was written. In this project, we have corrected this by changing the definition of drift. In this project, drift means when we update the weights of source stream instances. We have proposed an algorithm for doing that.
### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact