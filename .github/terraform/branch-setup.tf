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

  lifecycle {
    create_before_destroy = true
  }
}
