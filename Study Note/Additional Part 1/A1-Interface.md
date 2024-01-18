# Part 2: A1 Interface related in Near-RT RIC Platform
- Goal : 
    - [x] Learning A1 Interface
- Useful Links:
    - [O-RAN.WG3.A1AP-v04.00](https://www.o-ran.org/specifications)
    - [O-RAN.WG3.A1GAP-v03.01](https://www.o-ran.org/specifications)

- Outcome (Study Note) : 
    - Learn about A1 Interface

***

## I. A1 in General
A1 is the **interface between** the Non-RT RIC and the Near-RT RIC.

The purpose of the A1 interface is :
* To enable the Non-RT RIC function to provide policy-based guidance, 
* ML model management, 
* Enrichment information to the Near-RT RIC function so that the RAN can optimize e.g. RRM under certain conditions.

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/S1hsRLUFT.png"/>
    <figcaption>Illustration of A1 and related interfaces in the O-RAN architecture.
    </figcaption>
</figure>

## II. A1 Services
### A. A1 Policy Management Service (A1-P)
The purpose of the A1 policies is to guide the RAN performance towards the overall goal expressed in RAN intent.

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/SkGOgPLFp.png"/>
</figure>
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:80%;" src="https://hackmd.io/_uploads/S1SCePIFp.png"/>
</figure>

### B. A1 Enrichment Information Service (A1-EI)
The A1 interface is used for discovery, request and delivery of A1 enrichment information.

The A1 interface is also used for the discovery of external enrichment information and the SMO / Non-RT RIC is responsible for the authentication of the source and the security of the direct connection.

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/r1z8bDIYp.png"/>
</figure>
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/HJodWP8KT.png"/>
</figure>

### C. A1 ML Model Management Service (A1-ML)
ML model is trained in **the SMO layer** and then used by the Near-RT RIC **to improve the optimization of the RAN**. The training of the ML model is handled by SMO internal functions. The input data for training is the same as the input data the Near-RT RIC will use for inference. The trained ML model is deployed by the SMO layer via the **O1 interface**. The performance evaluation resulting from the execution of the ML model, and the handling of explicit feedback from the ML model itself, is based on O1 observability.

## III. A1 Interface
The A1 interface is an **open logical interface** within O-RAN architecture between the Non-RT RIC functionality in the SMO and the Near-RT RIC functionality in the RAN.

**Objectives**:
1. Connect Non-RT RIC in SMO with Near-RT RIC in diverse Radio Access Networks from different manufacturers.
2. Provide policies for individual UEs or UE groups.
3. Offer fundamental feedback on policy state, allowing Non-RT RIC to monitor policy usage.
4. Supply required enrichment information to Near-RT RIC.

**Capabilities**:
- Transfer of policy management information from Non-RT RIC to Near-RT RIC;
- Policy feedback from Near-RT RIC to Non-RT RIC;
- Discovery and request of A1 enrichment information from Near-RT RIC to Non-RT RIC and delivery of A1 enrichment information from Non-RT RIC to Near-RT RIC.

### A. Signaling Procedures
**Policy Related** Procedure:
- Query policy type identifiers procedure;
- Query policy type procedure;
- Query policy type status procedure;
- Notify policy type status procedure;
- Create policy procedure;
- Query policy identifiers procedure; 
- Query policy procedure;
- Update policy procedure;
- Delete policy procedure;
- Query policy status procedure; 
- Feedback policy procedure.

**EI Discovery in A1 Enrichment** Procedure:
- Query EI type identifiers; 
- Query EI type;
- Query EI type status;
- Notify EI type status.

**EI Job Control in A1 Enrichment** Procedure:
- Query EI job identifiers; 
- Create EI job;
- Query EI job;
- Update EI job;
- Delete EI job;
- Query EI job status;
- Notify EI job status.

**EI Delivery in A1 Enrichment** Procedure:
- Deliver EI job result.

### B. A1 Interface Protocol Structure
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:80%;" src="https://hackmd.io/_uploads/rypQEuLFa.png"/>
</figure>
