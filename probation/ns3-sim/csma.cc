/*
 NETWORK SIMULATOR 3 FOR BEGINNERS
 For support simulation in "CSMA (LAN Topology)" simulation.
*/

/*
 * Illustration of topology
 *
 * n0 n1 n2 n3 n4
 * |  |  |  |  |
 * ==================
 * LAN 10.1.1.0
 */

#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/csma-module.h"
#include "ns3/internet-module.h"
#include "ns3/applications-module.h"
#include "ns3/netanim-module.h" // Entered for animation configuration and output file

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("CsmaScript");

int main (int argc, char *argv[])
{
    bool verbose = true;
    uint32_t nCsma = 5;

    CommandLine cmd;
    cmd.AddValue ("nCsma", "Number of CSMA nodes/devices", nCsma);
    cmd.AddValue ("verbose", "Tell echo applications to log if true", verbose);

    cmd.Parse (argc, argv);

    if (verbose)
    {
        LogComponentEnable ("UdpEchoClientApplication", LOG_LEVEL_INFO);
        LogComponentEnable ("UdpEchoServerApplication", LOG_LEVEL_INFO);
    }

    NodeContainer csmaNodes;
    csmaNodes.Create (nCsma);

    CsmaHelper csma;
    csma.SetChannelAttribute ("DataRate", StringValue ("100Mbps"));
    csma.SetChannelAttribute ("Delay", TimeValue (NanoSeconds (6560)));

    NetDeviceContainer csmaDevices;
    csmaDevices = csma.Install (csmaNodes);

    InternetStackHelper stack;
    stack.Install (csmaNodes);

    Ipv4AddressHelper address;
    address.SetBase ("10.1.1.0", "255.255.255.0");

    Ipv4InterfaceContainer csmaInterfaces;
    csmaInterfaces = address.Assign (csmaDevices);

    UdpEchoServerHelper echoServer (9);
    ApplicationContainer serverApps = echoServer.Install (csmaNodes.Get (4));
    serverApps.Start (Seconds (1.0));
    serverApps.Stop (Seconds (10.0));

    UdpEchoClientHelper echoClient (csmaInterfaces.GetAddress (4), 9);
    echoClient.SetAttribute ("MaxPackets", UintegerValue (1));
    echoClient.SetAttribute ("Interval", TimeValue (Seconds (1.0)));
    echoClient.SetAttribute ("PacketSize", UintegerValue (1024));

    ApplicationContainer clientApps = echoClient.Install (csmaNodes.Get (0));
    clientApps.Start (Seconds (2.0));
    clientApps.Stop (Seconds (10.0));

    csma.EnablePcap ("csma", csmaDevices.Get (0), true);

    // Animation configuration lines
    AnimationInterface anim ("csma.xml");
    anim.SetConstantPosition (csmaNodes.Get(0), 0.0, 50.0 );
    anim.SetConstantPosition (csmaNodes.Get(1), 25.0, 50.0 );
    anim.SetConstantPosition (csmaNodes.Get(2), 50.0, 50.0 );
    anim.SetConstantPosition (csmaNodes.Get(3), 75.0, 50.0
