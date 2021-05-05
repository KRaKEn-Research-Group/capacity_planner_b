$nodeData = Get-Content "./nodes.txt"

$nodeData = $nodeData | ConvertFrom-Json

$distanceHash = @{}

Foreach($node in $nodeData.instance.network.nodes.node){    $tempId = $node."-id"
    $distanceHash."$tempId"= @()
    $tempX = $node.cx
    $tempY = $node.cx
    Foreach($node2 in $nodeData.instance.network.nodes.node){
        $distanceHash."$tempId" += [math]::Sqrt(($tempX - $node2.cx)*($tempX - $node2.cx) + ($tempY - $node2.cy)*($tempY - $node2.cy))
    }
}

$distanceHash | ConvertTo-Json | Out-File "DistanceMatrix.json"