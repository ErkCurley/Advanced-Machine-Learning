library(cloudml)


# cloudml_train("Cloud ML Folder/cats-and-dogs.R",master_type="standard_gpu")
job <- cloudml_train("cats-and-dogs.R", master_type="standard_gpu")

job_status(job)

view_run()
