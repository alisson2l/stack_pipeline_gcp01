resource "google_storage_bucket" "gcs_bucket"{
  name = "test-bucket-random-1001123"
  location = var.region
}