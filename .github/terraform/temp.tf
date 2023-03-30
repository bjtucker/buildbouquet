provider "github" {}

data "github_repository" "current" {
  full_name = "${github.repository}"
}

resource "github_branch_protection" "main" {
  repository_id = data.github_repository.current.id
  pattern       = "main"

  required_status_checks {
    strict = true
    contexts = [
      "continuous-integration",
    ]
  }

  enforce_admins = true

  required_pull_request_reviews {
    require_code_owner_reviews = true
  }
}
