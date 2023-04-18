from common_pb2 import LinkCodeRecord, Name, SceneRecord, SceneStatus, PropertyRecord, Contact, BusinessRecord, LinkCodeUsage
from common_pb2 import RenderingService, RenderingRecord, Address

import enum

def build_address():
  return Address(
    line_1="{{line_1}}", 
    line_2="{{line_2}}", 
    city="{{city}}", 
    post_code="{post_code}", 
    state_province_county="{{state_province_county}}",
    country_code="{{country_code}}"
  )

def build_business_record():
  return BusinessRecord(
    name="{{BUSINESS NAME}}",
    contact=Contact(),
    address=build_address()
  )

def build_property_record():
  return PropertyRecord(
    name="{{PROPERTY NAME}}", 
    address=build_address(), 
    builder=build_business_record()
  )

def build_rendering_record():
  return RenderingRecord(
    rendering=RenderingService.EAGLE_3D,
    path="https://connector.eagle3dstreaming.com/v5/avedis/RH_Hudson_5_0_LM/RH_Hudson"
  )

def build_rendering_record_pilot():
  return RenderingRecord(
    rendering=RenderingService.EAGLE_3D,
    path="https://connector.eagle3dstreaming.com/v5/avedis/P01_SB_v009/Pilot_01"
  )


def build_scene_record():
  return SceneRecord(
    name="{{scene_name}}",
    property=build_property_record(),
    status=SceneStatus.COMPLETED,
    rendering=build_rendering_record_pilot()
  )

class MockLinkType(enum.Enum):
   PUBLIC = 1
   PERSONAL = 2

def build_link_code_record(type: MockLinkType):
  match type:
    case MockLinkType.PUBLIC:
      
      return LinkCodeRecord(
        scene=build_scene_record(),
        usage=LinkCodeUsage.PUBLIC,
      )

    case MockLinkType.PERSONAL:
      return LinkCodeRecord(
        recipient_name=Name(first_name="John", last_name="Smith"),
        scene=build_scene_record(),
        usage=LinkCodeUsage.PERSONAL,
      ) 

def build_holt_link_code_record():
  return LinkCodeRecord(
      scene=SceneRecord(
      name="HOLT_01",
      property=PropertyRecord(
        name="Stone's Throw The 1609", 
        address=Address(
          line_1="Stone's Throw", 
          line_2="The 1609",
          line_3="3 Bed + 2.5 Bath + 2 Car Garage"
        ), 
        builder=BusinessRecord(
          name="Holt Homes"
        )
      ),
      status=SceneStatus.COMPLETED,
      rendering=RenderingRecord(
        rendering=RenderingService.EAGLE_3D,
        path="https://connector.eagle3dstreaming.com/v5/avedis/RH_Hudson_5_0_LM/RH_Hudson"
      )
    ),
    usage=LinkCodeUsage.PUBLIC,
  )

def build_kronkite_link_code_record():
  return LinkCodeRecord(
      scene=SceneRecord(
      name="CRONKHITE_1",
      property=PropertyRecord(
        name="The Waterton", 
        address=Address(
          line_1="The Waterton", 
          line_3="3 Bed + 2.5 Bath + 1 Car Garage"
        ), 
        builder=BusinessRecord(
          name="Cronkhite"
        )
      ),
      status=SceneStatus.COMPLETED,
      rendering=RenderingRecord(
        rendering=RenderingService.EAGLE_3D,
        path="https://connector.eagle3dstreaming.com/v5/avedis/CH_Waterton_v001/CH_Waterton"
      )
    ),
    usage=LinkCodeUsage.PUBLIC,
  )

def build_pinwheel_link_code_record():
  return LinkCodeRecord(
      scene=SceneRecord(
      name="HOLT_02",
      property=PropertyRecord(
        name="Stone's Throw The Pinwheel 2167", 
        address=Address(
          line_1="Stone's Throw", 
          line_2="The Pinwheel 2167",
          line_3="3 Bed + 2.5 Bath + 2 Car Garage"
        ), 
        builder=BusinessRecord(
          name="Holt Homes"
        )
      ),
      status=SceneStatus.COMPLETED,
      rendering=RenderingRecord(
        rendering=RenderingService.EAGLE_3D,
        path="https://connector.eagle3dstreaming.com/v5/avedis/HH_ST_2167_v002/HH_ST_Pinwheel_2167"
      )
    ),
    usage=LinkCodeUsage.PUBLIC,
  )

def build_hillmont_link_code_record():
  return LinkCodeRecord(
      scene=SceneRecord(
      name="TOLLBROTHERS_01",
      property=PropertyRecord(
        name="Henley Hillmont", 
        address=Address(
          line_1="Henley", 
          line_2="Hillmont",
          line_3="3 Bed + 3.5 Bath + 2 Car Garage"
        ), 
        builder=BusinessRecord(
          name="Toll Brothers"
        )
      ),
      status=SceneStatus.COMPLETED,
      rendering=RenderingRecord(
        rendering=RenderingService.EAGLE_3D,
        path="https://connector.eagle3dstreaming.com/v5/avedis/TB_H_Hillmont_SB_v002/TollBrothers_Hillmont"
      )
    ),
    usage=LinkCodeUsage.PUBLIC,
  )

def build_kourtney_link_code_record():
  return LinkCodeRecord(
      scene=SceneRecord(
      name="TOLLBROTHERS_02",
      property=PropertyRecord(
        name="Henley Ko", 
        address=Address(
          line_1="Henley", 
          line_2="Kourtney",
          line_3="4 Bed + 3.5 Bath + 2 Car Garage"
        ), 
        builder=BusinessRecord(
          name="Toll Brothers"
        )
      ),
      status=SceneStatus.COMPLETED,
      rendering=RenderingRecord(
        rendering=RenderingService.EAGLE_3D,
        path="https://connector.eagle3dstreaming.com/v5/avedis/TB_H_Kourtney_SB_v002/TollBrothers_Kourtney"
      )
    ),
    usage=LinkCodeUsage.PUBLIC,
  )