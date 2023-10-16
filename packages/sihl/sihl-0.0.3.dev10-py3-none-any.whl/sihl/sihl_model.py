from typing import Tuple, List, Union

from torch import Tensor, nn


class SihlModel(nn.Module):
    def __init__(
        self, backbone: nn.Module, neck: Union[nn.Module, None], heads: List[nn.Module]
    ) -> None:
        super().__init__()
        self.backbone = backbone
        self.neck = neck
        self.heads = nn.ModuleList(heads)

    def forward(self, input: Tensor) -> List[Union[Tensor, Tuple[Tensor, ...]]]:
        x = self.backbone(input)
        if self.neck is not None:
            x = self.neck(x)
        return [head(x) for head in self.heads]
