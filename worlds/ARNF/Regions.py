from typing import Dict, List, NamedTuple

class ARNFRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, ARNFRegionData] = {
    "Menu": ARNFRegionData(["NormalMode"]),
    "NormalMode": ARNFRegionData(["Victory"]),
    "Victory": ARNFRegionData()
}
