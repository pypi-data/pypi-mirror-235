"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.saas_target_namespace import (
    SaasTargetNamespace,
)


DEFINITION = """
fragment CommonJumphostFields on ClusterJumpHost_v1 {
  hostname
  knownHosts
  user
  port
  remotePort
  identity {
    ... VaultSecret
  }
}

fragment SaasTargetNamespace on Namespace_v1 {
  name
  labels
  delete
  path
  environment {
    name
    labels
    parameters
    secretParameters {
      name
      secret {
        ...VaultSecret
      }
    }
  }
  app {
    name
    parentApp {
      name
    }
    labels
    selfServiceRoles {
      name
    }
    serviceOwners {
      name
      email
    }
  }
  cluster {
    name
    serverUrl
    internal
    insecureSkipTLSVerify
    labels
    jumpHost {
      ...CommonJumphostFields
    }
    automationToken {
      ...VaultSecret
    }
    clusterAdminAutomationToken {
      ...VaultSecret
    }
    disable {
      integrations
    }
    spec {
      region
    }
    externalConfiguration {
      labels
    }
  }
  skupperSite {
    delete
  }
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query SaasFileTargetNamespaces {
  namespaces: namespaces_v1 {
    ...SaasTargetNamespace
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union = True
        extra = Extra.forbid


class SaasFileTargetNamespacesQueryData(ConfiguredBaseModel):
    namespaces: Optional[list[SaasTargetNamespace]] = Field(..., alias="namespaces")


def query(query_func: Callable, **kwargs: Any) -> SaasFileTargetNamespacesQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        SaasFileTargetNamespacesQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return SaasFileTargetNamespacesQueryData(**raw_data)
