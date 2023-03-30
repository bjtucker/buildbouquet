provider "github" {}

data "github_repository" "current" {
  full_name = "bjtucker/buildbouquet"
}

resource "github_branch_protection" "main" {
  lifecycle {
    create_before_destroy = true
  }

  repository_id = data.github_repository.current.id
  pattern       = "main"

  required_status_checks {
    strict = true
    contexts = [
      "continuous-integration",
    ]
  }

  enforce_admins = true
}
