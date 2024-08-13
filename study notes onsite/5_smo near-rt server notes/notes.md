


##  Turn on/off Cell manually using Netconf
```
python3
```
```
1 | from ncclient import manager
2 | sm0 = manager.connect(host='192.168.8.28', port="31237", timeout=5, username="root")
```

### at "energySavingControl", turn on cell = "isNotEnergySaving" and turn off cell = "isEnergySaving"
```
conf= '''
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
<ManagedElement xmlns="urn:3gpp:sa5:_3gpp-common-managed-element">
  <id>1193046</id>
  <GNBCUCPFunction xmlns="urn:3gpp:sa5:_3gpp-nr-nrm-gnbcucpfunction">
    <id>1</id>
    <NRCellCU xmlns="urn:3gpp:sa5:_3gpp-nr-nrm-nrcellcu">
      <id>2</id>
      <CESManagementFunction xmlns="urn:3gpp:sa5:_3gpp-nr-nrm-cesmanagementfunction">
        <id>2</id>
        <attributes>
          <energySavingState>isNotEnergySaving</energySavingState>
          <energySavingControl>toBeEnergySaving</energySavingControl>
        </attributes>
      </CESManagementFunction>
    </NRCellCU>
  </GNBCUCPFunction>
</ManagedElement>
</config>
'''
```
```
smo.edit_config (target = "running", config=conf)
```