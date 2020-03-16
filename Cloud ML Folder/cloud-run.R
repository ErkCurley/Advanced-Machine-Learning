library(cloudml)

# gs_copy("Data", "gs://ml-project-267916/training-data", recursive = TRUE)

cloudml_train("cats-and-dogs.R", master_type="standard_gpu")

job_status()

job_collect()

view_run()