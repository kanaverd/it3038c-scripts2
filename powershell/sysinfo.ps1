
function getIP {
(get-netipaddress).ipv4address | Select-String "192*"
}
write-host(getIP)