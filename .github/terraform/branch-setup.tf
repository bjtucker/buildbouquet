data "github_repository" "current" {
  name = "buildbouquet"
}

resource "github_branch_protection" "main" {
  repository_id = data.github_repository.current.node_id
  pattern       = "main"

  required_pull_request_reviews {
    dismiss_stale_reviews = false
    require_code_owner_reviews = false
  }
  
  required_status_checks {
    strict = true
    contexts = [
      "Lint Markdown Files / markdownlint",
      "branch-setup / terraform-plan",
    ]
  }


  lifecycle {
    create_before_destroy = true
  }
}
