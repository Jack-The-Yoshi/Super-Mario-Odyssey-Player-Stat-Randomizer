import random
import re
import sys
import tempfile
import contextlib
import io
import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from importlib import metadata as importlib_metadata


DEFAULT_PLAYERCONST = r"""
  AdditionalSpeedLimit: 30.00000
  AnimFrameRateMaxDash: 4.00000
  AnimFrameRateMaxDashFast: 5.00000
  AnimFrameRateMaxRun: 3.50000
  AnimFrameRateMaxRun2D: 2.50000
  AnimFrameRateMinRun: 1.00000
  AnimFrameRateMinRun2D: 1.00000
  AnimFrameRateRange2D: 10.00000
  AnimFrameRateRunStart: 2.00000
  AnimFrameRateSpeedMax: 26.00000
  AnimFrameRateSpeedMin: 6.00000
  BrakeOnCounterBorder: !l 10
  BrakeOnSpeedRate: 0.50000
  BrakeTurnStartFrame: !l 5
  BrakeTurnStartFrame2D: !l 5
  CapCatchPopGravity: 0.80000
  CapCatchPopPower: 10.00000
  CapChildLocalOffset: 100.00000
  CapFriction: 0.20000
  CapHeadSpringJumpGravity: 1.20000
  CapHeadSpringJumpGravityHigh: 1.00000
  CapHeadSpringJumpPower: 18.00000
  CapHeadSpringJumpPowerHigh: 22.00000
  CapHeadSpringSpeedMax: 16.00000
  CapInterpolateFrame: !l 15
  CapLeapFrogJumpGravity: 1.00000
  CapLeapFrogJumpPower: 32.00000
  CapLeapFrogJumpPowerAir: 26.00000
  CapLimitDegree: 15.00000
  CapManHeroEyesWaitAppearFrame: !l 330
  CapStability: 0.75000
  CapTransFriction: 0.25000
  CapTransLimit: 10.00000
  CapTransStability: 0.95000
  CenterTiltRateMax: 0.00000
  CoinDashSpeed: 6.00000
  CoinDashSpeedLimit: 6.00000
  CollisionHitDownAngleH: 55.00000
  CollisionHitDownEscapeAngleV: 30.00000
  CollisionRadius: 55.00000
  CollisionRadiusSquat: 45.00000
  CollisionRadiusStand: 45.00000
  CollisionResetLimit: 20.00000
  CollisionSmallStepHeight: 25.00000
  ContinuousJumpCount: !l 3
  ContinuousJumpPowerMin: 19.50000
  ContinuousJumpPreInputFrame: !l 5
  ContinuousJumpTimer: !l 10
  ContinuousLongJumpCount: !l 3
  ContinuousLongJumpTimer: !l 15
  DamageCancelFrame: !l 45
  DamageFireCeilHitSpeed: 1.00000
  DamageFireGravity: 0.90000
  DamageFireJumpMoveSpeed: 10.00000
  DamageFireJumpPower1st: 20.00000
  DamageFireJumpPower2nd: 20.00000
  DamageFireNoGravityFrame: !l 20
  DamageFireRunAnimRate: 0.30000
  DamageFireRunBrakeFrame: 20.00000
  DamageFireRunSpeed: 18.00000
  DamageFireRunTime: !l 60
  DamageInvalidCount: !l 240
  DamageInvalidCountAbyss: !l 120
  DamageInvalidCountRecovery: !l 20
  DamageSwimBrakeRateGround: 0.95000
  DamageSwimCancelFrame: !l 50
  DamageSwimGravity: 0.02000
  DamageSwimPushPower: 3.00000
  DamageSwimSurfaceCancelFrame: !l 40
  DamageSwimSurfaceGravity: 0.95000
  DamageSwimSurfaceHopPower: 20.00000
  DamageSwimSurfaceLandBrake: 0.05000
  DamageSwimSurfaceLandEndSpeed: 1.00000
  DamageSwimSurfaceLandSpeed: 5.00000
  DamageSwimSurfacePushPower: 4.00000
  DashAccelFrame2D: !l 30
  DashBlendRange: 1.00000
  DashBorderSpeed: 15.00000
  DashFastBlendRange: 1.00000
  DashFastBorderSpeed: 20.00000
  DashJudgeSpeed: 14.50000
  DashMaxSpeed2D: 17.00000
  DeadWipeStartAbyss: !l 30
  DeadWipeStartAbyssWithCapMsg: !l 90
  DeadWipeStartDamage: !l 30
  DeadWipeStartIceWater: !l 30
  DeadWipeStartNoOxygen: !l 30
  DeadWipeStartPress: !l 40
  DeadWipeStartSandSink: !l 30
  DeadWipeWaitAbyss: !l 30
  DeadWipeWaitAbyssWithCapMsg: !l 30
  DeadWipeWaitDamage: !l 96
  DeadWipeWaitIceWater: !l 96
  DeadWipeWaitNoOxygen: !l 96
  DeadWipeWaitPress: !l 96
  DeadWipeWaitSandSink: !l 96
  DiveTrampleCancelFrame: !l 20
  DiveTramplePower: 11.00000
  DownFallFrameMin: !l 5
  EnableActionFrameCapCatch: !l 10
  ExtendFrame: !l 10
  FallSpeedMax: 35.00000
  FallWallScaleVelocity: 0.50000
  FrictionAir: 0.99000
  FrictionAttack: 0.90000
  GrabCeilBodyRadius: 50.00000
  GrabCeilEnableFallSnapFrame: !l 30
  GrabCeilEnableJumpEnergy: 6.50000
  GrabCeilEnableJumpEnergyMax: 10.00000
  GrabCeilEnableNextFrame: !l 10
  GrabCeilInputPowerBorder: 6.00000
  GrabCeilJumpForceAngle: 135.00000
  GrabCeilJumpGravity: 1.00000
  GrabCeilJumpInvalidFrame: !l 10
  GrabCeilJumpMoveMax: 15.00000
  GrabCeilJumpMoveMin: 15.00000
  GrabCeilJumpPower: 20.00000
  GrabCeilLeavePopGravity: 1.20000
  GrabCeilLeavePopPower: 3.00000
  GrabCeilLeaveSpeedMin: 1.00000
  GrabCeilRange: 100.00000
  GrabCeilReverseInputBorder: 6.00000
  GrabCeilSwingStartOffset: 1.00000
  GrabCeilSwingWaitEnergy: 6.50000
  Gravity: 3.00000
  GravityAir: 1.50000
  GravityDamage: 0.95000
  GravityMove: 7.00000
  GravitySpinAir: 0.30000
  GravityWallSlide: 0.50000
  GroundSpinAccelRate: 0.50000
  GroundSpinBrakeRate: 0.95000
  GroundSpinFrame: !l 90
  GroundSpinMoveSpeedMax: 8.00000
  HeadSlidingBrake: 0.50000
  HeadSlidingGravityAir: 2.00000
  HeadSlidingJump: 28.00000
  HeadSlidingSideAccel: 0.12500
  HeadSlidingSpeed: 20.00000
  HeadSlidingSpeedMin: 2.50000
  HillAccelAddFrame: !l 60
  HillAccelSubAngleMax: 20.00000
  HillAccelSubAngleMin: 0.00000
  HillAccelSubFrame: !l 100
  HillAddSpeed: 15.00000
  HillAngleSpeedMax: 26.00000
  HillAngleSpeedMin: 21.00000
  HillPoseDegreeMax: 45.00000
  HillSubSpeed: 0.00000
  HipDropGravity: 45.00000
  HipDropHeight: 40.00000
  HipDropLandCancelFrame: !l 24
  HipDropMsgInterval: !l 8
  HipDropSpeed: 45.00000
  HipDropSpeedMax: 45.00000
  HopPowerDamage: 12.00000
  IKBlendFrameRun: !l 60
  IKBlendRateRunMax: 0.95000
  IKBlendRateRunMin: 0.85000
  IceAccelFrame: !l 60
  IceBrakeFrame: !l 120
  IceBrakeFrameHigh: !l 60
  IceBrakeFrameWall: !l 15
  IceRoundAccelFrame: !l 20
  IceRoundAccelFrameFast: !l 1
  IceRoundBrakeFrame: !l 30
  IceRoundFastDegree: 45.00000
  IceRoundLimitDegree: 25.00000
  IceRoundMinDegree: 3.00000
  IceWaterDamageInterval: !l 300
  IceWaterRecoveryFrame: !l 70
  JumpAccelBack: 1.00000
  JumpAccelFront: 0.50000
  JumpAccelTurn: 0.30000
  JumpBaseSpeedMax: 24.00000
  JumpGravity: 1.50000
  JumpGravity2nd: 1.50000
  JumpGravity3rd: 1.00000
  JumpGravityCapCatch: 1.30000
  JumpGravityForceRun: 1.00000
  JumpHipDropPermitBeginFrame: !l 5
  JumpHipDropPermitEndFrame: !l 30
  JumpHipDropPower: 40.00000
  JumpInertiaRate: 0.70000
  JumpMoveSpeedMax: 30.00000
  JumpMoveSpeedMin: 11.00000
  JumpPowerCapCatch: 22.00000
  JumpPowerForceRun: 18.00000
  JumpPowerMax: 19.50000
  JumpPowerMax2DArea: 27.50000
  JumpPowerMax2nd: 21.00000
  JumpPowerMax3rd: 25.00000
  JumpPowerMaxBorder2D: 18.00000
  JumpPowerMin: 17.00000
  JumpPowerMin2DArea: 23.50000
  JumpPowerMinBorder2D: 12.00000
  JumpTurnAccelFrame: !l 20
  JumpTurnAccelFrameFast: !l 1
  JumpTurnAngleFast: 135.00000
  JumpTurnAngleFastLimit: 25.00000
  JumpTurnAngleLimit: 6.00000
  JumpTurnAngleStart: 1.00000
  JumpTurnBrakeFrame: !l 10
  LongFallDistance: 3000.00000
  LongJumpAccel: 0.25000
  LongJumpBrake: 0.50000
  LongJumpGravity: 0.48000
  LongJumpInitSpeed: 14.00000
  LongJumpJumpPow: 12.00000
  LongJumpMovePow: 4.00000
  LongJumpSideAccel: 0.25000
  LongJumpSpeed: 23.00000
  LongJumpSpeedMin: 2.50000
  LookAtEyeAngleMaxH: 85.00000
  LookAtEyeAngleMaxV: 60.00000
  LookAtEyeAngleMinH: 35.00000
  LookAtEyeAngleMinInSightH: 10.00000
  LookAtEyeAngleMinInSightV: 10.00000
  LookAtEyeAngleMinV: 10.00000
  LookAtEyeDistance: 500.00000
  LookAtEyeKeepFrame: !l 30
  LookAtEyeKeepFrameInSight: !l 0
  LookAtEyeKeepFrameWait: !l 120
  MoveAnimSpeedMax: 25.00000
  MustacheChildLocalOffset: 100.00000
  MustacheFriction: 0.80000
  MustacheLimitDegree: 10.00000
  MustacheStability: 0.30000
  NormalAccelFrame: !l 40
  NormalAccelFrame2D: !l 15
  NormalBrakeFrame: !l 10
  NormalBrakeFrame2D: !l 10
  NormalDashAnimFrame: !l 15
  NormalDashAnimFrame2D: !l 15
  NormalMaxSpeed: 14.00000
  NormalMaxSpeed2D: 10.00000
  NormalMinSpeed: 3.00000
  NormalMinSpeed2D: 3.00000
  NoseChildLocalOffset: 50.00000
  NoseFriction: 0.80000
  NoseLimitDegree: 45.00000
  NoseStability: 0.10000
  ObjLeapFrogJumpPower: 20.00000
  ObjLeapFrogJumpPowerHigh: 25.00000
  OxygenDamageInterval: !l 300
  OxygenNoReduceFrame: !l 60
  OxygenRecoveryFrame: !l 30
  OxygenReduceFrame: !l 1380
  PoleClimbCatchRange: 50.00000
  PoleClimbCatchRangeMax: 100.00000
  PoleClimbCatchRangeMin: 10.00000
  PoleClimbDownFrame: !l 1
  PoleClimbDownKeepTime: !l 30
  PoleClimbDownSpeed: 10.00000
  PoleClimbDownSpeedFast: 15.00000
  PoleClimbDownSpeedSwing: 20.00000
  PoleClimbInputDegreeMove: 50.00000
  PoleClimbInputRepeatAngle: 10.00000
  PoleClimbJointAngleMax: 25.00000
  PoleClimbJointAngleMin: -25.00000
  PoleClimbJointRangeMax: 80.00000
  PoleClimbJointRangeMin: 15.00000
  PoleClimbMoveWallDegree: 5.00000
  PoleClimbPreInputSwing: !l 15
  PoleClimbTurnDist: 40.00000
  PoleClimbTurnFrame: !l 15
  PoleClimbTurnStopFrame: !l 5
  PoleClimbUpFrame: !l 25
  PoleClimbUpFrameFast: !l 17
  PoleClimbUpFrameSwing: !l 12
  PoleClimbUpMargine: 40.00000
  PoleClimbUpSpeed: 100.00000
  PoleTopEndFrame: !l 10
  PoleTopEndUnderOffsetY: 60.00000
  PoleTopStartFrame: !l 10
  PoleTopTurnSpeed: 4.00000
  PreInputFrameCapThrow: !l 10
  PushPower: 20.00000
  PushPowerDamage: 2.00000
  QuickTurnJumpFrame: !l 20
  ReflectCeilingPower: 17.00000
  ReflectTossPower: 5.00000
  ReflectUpperPunchScaleH: 0.40000
  RollingAnimBorderSpeedMax: 35.00000
  RollingAnimBorderSpeedMin: 5.00000
  RollingAnimFrameRateMax: 1.00000
  RollingAnimFrameRateMin: 0.20000
  RoundAccelFrame: !l 20
  RoundAccelFrameFast: !l 5
  RoundAccelFrameForceFast: !l 10
  RoundBrakeFrame: !l 20
  RoundBrakeFrameForce: !l 3
  RoundFastDegree: 45.00000
  RoundFastDegreeForce: 45.00000
  RoundLimitDegree: 8.50000
  RoundLimitDegreeForce: 4.00000
  RoundLimitDegreeForceFast: 4.00000
  RoundLimitDegreeMin: 6.50000
  RoundMinDegree: 0.50000
  RunAccelAverageScale: 0.50000
  RunAccelFrameContinuousThrow: !l 60
  RunAfterTurnFrame: !l 30
  RunAfterTurnScale: 0.50000
  RunAfterTurnSpeedMax: 17.00000
  RunBlendRange: 2.00000
  RunBorderSpeed: 8.00000
  RunDeepDownFrame: !l 10
  RunDeepDownMargine: !l 10
  RunSkateAnimSpeedOffset: 5.00000
  RunSpeedMaxContinuousThrow: 16.00000
  RunStartBlendFrame: !l 5
  RunStartPlayFrameScale: 1.00000
  RunTimeContinuousThrow: !l 20
  SandSinkBorderMax: 0.50000
  SandSinkBorderMin: 0.00000
  SandSinkBorderRateMax: 0.50000
  SandSinkBorderRateMin: 0.00000
  SandSinkBrakeHeightH: !l 100
  SandSinkBrakeHeightV: !l 60
  SandSinkBrakeMaxH: 0.10000
  SandSinkBrakeMaxV: 0.10000
  SandSinkBrakeMinH: 0.60000
  SandSinkBrakeMinV: 1.00000
  SandSinkCapThrow: 30.00000
  SandSinkDeadTime: !l 240
  SandSinkFrameRateMax: 0.50000
  SandSinkFrameRateMin: 4.00000
  SandSinkHeight: 200.00000
  SeparateCheckHeight: 200.00000
  SeparateEnableThrowHeight: 45.00000
  SeparateOffsetLerpRate: 0.25000
  ShadowDropHeightScale: 1.20000
  ShadowDropLengthExtend: 10000.00000
  ShadowDropLengthMax: 4000.00000
  ShadowDropLengthMin: 20.00000
  ShadowDropNormalAdd: 300.00000
  SlerpQuatGrav: 0.40000
  SlerpQuatRate: 0.15000
  SlerpQuatRateSpinAir: 0.10000
  SlerpQuatRateWait: 0.15000
  SlideInvalidFrame: !l 15
  SlopeForceFrame: !l 30
  SlopeRollingAccel: 0.60000
  SlopeRollingAccelOnSkate: 0.90000
  SlopeRollingAgainst: 0.50000
  SlopeRollingAnglePowerMax: 30.00000
  SlopeRollingBrake: 0.99800
  SlopeRollingBrakeOnSkate: 0.99900
  SlopeRollingEndBrake: 0.95000
  SlopeRollingEndBrakeEndSpeed: 10.00000
  SlopeRollingFrameMin: !l 45
  SlopeRollingFrameMinBoost: !l 30
  SlopeRollingMaxSpeed: 35.00000
  SlopeRollingReStartAccel: 6.00000
  SlopeRollingReStartCharge: !l 40
  SlopeRollingReStartForce: !l 60
  SlopeRollingReStartInterval: !l 15
  SlopeRollingReStartMaxAdd: 3.00000
  SlopeRollingReStartSwing: !l 0
  SlopeRollingSideAccel: 0.40000
  SlopeRollingSideAccelOnSkate: 0.60000
  SlopeRollingSideBrake: 0.98500
  SlopeRollingSideMaxSpeed: 10.00000
  SlopeRollingSpeedBoost: 30.00000
  SlopeRollingSpeedEnd: 17.00000
  SlopeRollingSpeedStart: 20.00000
  SlopeRollingStartJumpPower: 12.00000
  SlopeRollingStartSlideSpeed: 1.00000
  SlopeRollingUnRollFrame: !l 5
  SlopeSlideAccel: 0.30000
  SlopeSlideAngleEnd: 10.00000
  SlopeSlideAngleStart: 26.00000
  SlopeSlideBrake: 0.90000
  SlopeSlideForceSideAccel: 0.20000
  SlopeSlideForceSideBrake: 0.96000
  SlopeSlideForceSideMaxSpeed: 3.00000
  SlopeSlideForceTurnDegree: 15.00000
  SlopeSlideMaxSpeed: 22.00000
  SlopeSlideSideAccel: 0.60000
  SlopeSlideSideBrake: 0.98000
  SlopeSlideSideMaxSpeed: 10.00000
  SlopeSlideSpeedEnd: 3.00000
  SlopeTurnDegree: 5.00000
  SpinAirJumpPower: 6.00000
  SpinAirSpeedMax: 7.00000
  SpinAttackFrame: !l 12
  SpinBrakeFrame: !l 15
  SpinBrakeRate: 0.95000
  SpinBrakeSideAccel: 0.50000
  SpinBrakeSideBrakeRate: 0.95000
  SpinBrakeSideMaxSpeedRate: 0.80000
  SpinCapThrowFrame: !l 12
  SpinCapThrowFrameAir: !l 8
  SpinCapThrowFrameContinuous: !l 2
  SpinCapThrowFrameSwim: !l 12
  SpinCapThrowFrameSwing: !l 7
  SpinFlowerJumpDownFallInitSpeed: 15.00000
  SpinFlowerJumpDownFallPower: 2.00000
  SpinFlowerJumpDownFallSpeedMax: 30.00000
  SpinFlowerJumpFallSpeedMax: 8.00000
  SpinFlowerJumpGravity: 0.10000
  SpinFlowerJumpMovePower: 1.00000
  SpinFlowerJumpNoInputBrake: 0.95000
  SpinFlowerJumpStayFrame: !l 80
  SpinFlowerJumpStaySpeedMax: 1.00000
  SpinFlowerJumpVelMax: 9.00000
  SpinJumpDownFallInitSpeed: 35.00000
  SpinJumpDownFallPower: 1.50000
  SpinJumpDownFallSpeedMax: 45.00000
  SpinJumpGravity: 0.40000
  SpinJumpMoveSpeedMax: 8.00000
  SpinJumpPower: 20.00000
  SpinRoundLimitDegree: 5.00000
  SquatAccelRate: 1.20000
  SquatBrakeEndSpeed: 3.50000
  SquatBrakeRate: 0.95000
  SquatBrakeRateOnSkate: 0.98500
  SquatBrakeSideAccel: 0.25000
  SquatBrakeSideAccelOnSkate: 0.10000
  SquatBrakeSideMaxSpeedRate: 0.50000
  SquatBrakeSideRate: 0.93000
  SquatBrakeSideRateOnSkate: 0.97500
  SquatJumpBackPower: 5.00000
  SquatJumpCeilSlideSpeed2D: 7.00000
  SquatJumpGravity: 1.00000
  SquatJumpMovePowerFront: 0.20000
  SquatJumpMovePowerSide: 0.20000
  SquatJumpMoveSpeedMax: 9.00000
  SquatJumpPower: 32.00000
  SquatWalkSpeed: 3.50000
  SquatWalkTurnFrame: !l 10
  SquatWalkTurnSpeed: 30.00000
  StandAngleMax: 70.00000
  StandAngleMin: 60.00000
  StickOnBrakeFrame: !l 120
  StickOnBrakeFrame2D: !l 60
  SwimBentForwardBlendRate: 0.05000
  SwimBentForwardMax: 30.00000
  SwimBentFrontBlendRate: 0.04000
  SwimBentFrontMax: 45.00000
  SwimBentSideBlendRate: 0.05000
  SwimBentSideMax: 60.00000
  SwimBentSpineMax: 40.00000
  SwimBrakeRateH: 0.97500
  SwimCenterOffset: 80.00000
  SwimDiveBrake: 0.87500
  SwimDiveButtonValidFrame: !l 10
  SwimDiveEndFrame: !l 5
  SwimDiveEndSpeed: 1.25000
  SwimDiveInBrakeH: 0.97000
  SwimDiveInBrakeV: 0.98700
  SwimDiveInKeepFrame: !l 10
  SwimDiveInRisePower: 0.50000
  SwimDiveInRiseSpeedMax: 3.00000
  SwimDiveInSurfaceHeight: 50.00000
  SwimDiveLandCancelFrame: !l 15
  SwimDiveLandCount: !l 0
  SwimDiveNoBrakeFrame: !l 15
  SwimDiveStartSpeed: 26.50000
  SwimFallInBrakeH: 0.95000
  SwimFallInBrakeV: 0.91000
  SwimFallInForceSurfaceFrame: !l 10
  SwimFallInSpeed: 15.00000
  SwimFallInvalidJumpFrame: !l 8
  SwimFallSpeedMax: 6.50000
  SwimFloorAccelH: 0.12500
  SwimFloorSpeedMaxH: 6.50000
  SwimFlowFieldBlend: 0.77600
  SwimGravity: 0.25000
  SwimGravityWalk: 1.00000
  SwimHeadInBrakeH: 0.98000
  SwimHeadInBrakeV: 0.92000
  SwimHeadInRisePower: 0.60000
  SwimHeadInRiseSpeedMax: 10.00000
  SwimHeadInSurfaceHeight: 50.00000
  SwimHeadSlidingBrake: 0.00000
  SwimHeadSlidingBrakeFrame: !l 45
  SwimHeadSlidingEndBrakeFrame: !l 30
  SwimHeadSlidingEndSpeedMin: !l 5
  SwimHeadSlidingFrame: !l 15
  SwimHeadSlidingGravity: 0.00000
  SwimHeadSlidingJump: 0.00000
  SwimHeadSlidingSideAccel: 0.12500
  SwimHeadSlidingSpeed: 15.00000
  SwimHeadSlidingSpeedEnd: 10.00000
  SwimHighAccelH: 0.25000
  SwimHighAccelPermitFrame: !l 35
  SwimHighSpeedMaxH: 7.50000
  SwimJumpHipDropAccelH: 0.25000
  SwimJumpHipDropBrakeV: 0.98000
  SwimJumpHipDropBrakeVCeiling: 0.50000
  SwimJumpHipDropCancelSpeed: 7.50000
  SwimJumpHipDropGravity: 0.20000
  SwimJumpHipDropMoveSpeedH: 3.00000
  SwimJumpHipDropPopJumpAdd: 7.00000
  SwimJumpHipDropPopSpeed: 8.00000
  SwimJumpHipDropSpeed: 27.00000
  SwimLowAccelH: 0.25000
  SwimLowSpeedMaxH: 6.50000
  SwimPaddleAnimInterval: !l 32
  SwimPaddleAnimMaxRate: 3.00000
  SwimPaddleAnimRateIntervalMax: !l 22
  SwimPaddleAnimRateIntervalMin: !l 5
  SwimRiseFrame: !l 10
  SwimRisePower: 0.60000
  SwimRiseSpeedMax: 7.50000
  SwimRotAccelFrame: !l 20
  SwimRotAccelFrameFast: !l 1
  SwimRotBrakeFrame: !l 30
  SwimRotFastAngle: 80.00000
  SwimRotSpeedChangeStart: 3.00000
  SwimRotSpeedForward: 3.00000
  SwimRotSpeedMax: 7.50000
  SwimRotStartAngle: 1.00000
  SwimRunSurfaceApproachBorderMax: 38.00000
  SwimRunSurfaceApproachBorderMin: 30.00000
  SwimRunSurfaceApproachLimit: 5.00000
  SwimRunSurfaceApproachRate: 0.50000
  SwimRunSurfaceApproachRateMin: 0.06000
  SwimRunSurfaceBaseHeight: 0.00000
  SwimRunSurfaceBrakeBorder: 35.00000
  SwimRunSurfaceBrakeH: 0.99500
  SwimSpinCapUpPower: 10.00000
  SwimSpinCapUpSpeedMax: 4.50000
  SwimSurfaceAccelH: 0.25000
  SwimSurfaceBaseHeight: 80.00000
  SwimSurfaceDamper: 0.94900
  SwimSurfaceDamperFrame: !l 25
  SwimSurfaceDamperStart: !l 25
  SwimSurfaceEnableJumpHeight: 160.00000
  SwimSurfaceEndDist: 200.00000
  SwimSurfaceGravity: 0.12500
  SwimSurfaceMoveBaseHeight: 80.00000
  SwimSurfaceMoveDamper: 0.94000
  SwimSurfaceMoveSpring: 0.01000
  SwimSurfacePreInputJumpFrame: !l 8
  SwimSurfaceSpeedMaxH: 9.00000
  SwimSurfaceSpinCapFrame: !l 45
  SwimSurfaceSpinCapSpeedMaxH: 13.00000
  SwimSurfaceSpring: 0.05000
  SwimSurfaceStartDist: 120.00000
  SwimTramplePower: 8.00000
  SwimWalkAnimFrameRateMax: 1.75000
  SwimWalkAnimFrameRateMin: 0.50000
  SwimWalkAnimMaxRate: 1.90000
  SwimWalkAnimMinRate: 0.20000
  SwimWalkAnimSpeedMax: 6.50000
  SwimWalkAnimSpeedMin: 1.00000
  SwimWalkMaxSpeed: 5.00000
  SwimWallCatchOffset: 100.00000
  SwimWallHitSpeedMinH: 3.00000
  Tall: 160.00000
  TiltEyeAngleScale: 0.40000
  TiltEyeBorderEnd: 0.25000
  TiltEyeBorderStart: 0.90000
  TiltPoseDegreeMax: 20.00000
  TrampleGravity: 1.75000
  TrampleGravity2D: 1.75000
  TrampleHighGravity: 1.00000
  TrampleHighGravity2D: 1.00000
  TrampleHighJumpPower: 25.00000
  TrampleHighJumpPower2D: 32.00000
  TrampleHipDropGravity: 1.50000
  TrampleHipDropJumpPower: 35.00000
  TrampleJumpCodePower: 57.00000
  TrampleJumpCodePowerSmall: 35.00000
  TrampleJumpPower: 20.00000
  TrampleJumpPower2D: 20.00000
  TrampleRisingBrakeVelH: 0.30000
  TurnEndSpeedRate2D: 1.00000
  TurnJumpAccel: 0.25000
  TurnJumpBrake: 0.50000
  TurnJumpGravity: 1.00000
  TurnJumpPower: 32.00000
  TurnJumpSideAccel: 0.07500
  TurnJumpVelH: 9.00000
  WaitPoseDegreeMax: 45.00000
  WallCatchDegree: 43.00000
  WallCatchHeightBottom: 150.00000
  WallCatchHeightEdgeTop: 120.00000
  WallCatchHipFriction: 0.90000
  WallCatchHipLimitDegree: 75.00000
  WallCatchHipLocalOffset: 100.00000
  WallCatchHipStability: 0.10000
  WallCatchInputRepeatAngle: 30.00000
  WallCatchKeepDegree: 45.00000
  WallCatchMoveDegree: 40.00000
  WallCatchMoveFrame: !l 10
  WallCatchMoveFrameFast: !l 8
  WallCatchMoveFrameSwing: !l 6
  WallCatchMoveHeightRange: 70.00000
  WallCatchMoveInterpolate: !l 10
  WallCatchMoveSpeed: 70.00000
  WallCatchStainAreaOffset: 100.00000
  WallClimbDegree: 40.00000
  WallClimbGravity: 15.00000
  WallClimbJumpEndFrame: !l 30
  WallClimbJumpGravity: 1.50000
  WallClimbJumpInvalidFrame: !l 12
  WallClimbJumpSpeedH: 3.00000
  WallClimbJumpSpeedV: 20.00000
  WallClimbJumpStartFrame: !l 5
  WallClimbStartFrame: !l 20
  WallFallJumpSpeed: 12.00000
  WallFollowAngleH: 20.00000
  WallFollowAngleV: 30.00000
  WallHeightLowLimit: 120.00000
  WallInhibitAfterPunch: !l 10
  WallJumpGravity: 0.95000
  WallJumpHSpeed: 8.60000
  WallJumpInvalidateInputFrame: !l 25
  WallJumpPower: 23.00000
  WallKeepDegree: 60.00000
  WallKeepFrame: !l 3
  WallPushFrame: !l 15
"""


class PlayerConstRandomizerApp:

    def __init__(self, root: tk.Tk) -> None:

        self.root = root
        self.root.title("Super Mario Odyssey Player Stat Randomizer")
        self.root.resizable(True, True)

        self.loaded_text: str = DEFAULT_PLAYERCONST

        self._build_ui()

    # ------------------------------------------------------------
    # UI
    # ------------------------------------------------------------

    def _build_ui(self) -> None:

        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="Super Mario Odyssey Player Stat Randomizer",
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="w", pady=(0, 10))

        ttk.Label(
            main,
            text=(
                "Randomizes Mario movement and physics values from PlayerConst.byml.\n"
                "Higher chaos levels produce more extreme gameplay."
            ),
            justify="left",
        ).pack(anchor="w", pady=(0, 10))

        settings_frame = ttk.LabelFrame(main, text="Randomization Settings", padding=10)
        settings_frame.pack(fill="x", pady=(0, 10))

        # ------------------------------------------------------------
        # Strength Slider
        # ------------------------------------------------------------

        ttk.Label(settings_frame, text="Randomization Strength:").grid(
            row=0, column=0, sticky="w", padx=(0, 8), pady=4
        )

        self.strength_var = tk.DoubleVar(value=0.30)

        self.strength_slider = ttk.Scale(
            settings_frame,
            from_=0.05,
            to=2.0,
            variable=self.strength_var,
            orient="horizontal",
            length=250,
            command=self._update_strength_label
        )

        self.strength_slider.grid(row=0, column=1, sticky="w", pady=4)

        self.strength_label = ttk.Label(settings_frame, text="0.30 (Balanced Chaos)")
        self.strength_label.grid(row=0, column=2, sticky="w", padx=(10, 0))

        # ------------------------------------------------------------
        # Seed
        # ------------------------------------------------------------

        ttk.Label(settings_frame, text="Seed:").grid(row=1, column=0, sticky="w")

        self.seed_var = tk.StringVar(value="")
        self.seed_entry = ttk.Entry(settings_frame, textvariable=self.seed_var, width=18)
        self.seed_entry.grid(row=1, column=1, sticky="w")

        ttk.Button(
            settings_frame,
            text="Generate Seed",
            command=self.generate_seed
        ).grid(row=1, column=2, sticky="w", padx=(10, 0))

        ttk.Label(
            settings_frame,
            text="Share this seed so other people can get the exact same randomization"
        ).grid(row=2, column=0, columnspan=3, sticky="w", pady=4)

        # ------------------------------------------------------------
        # Advanced Toggle
        # ------------------------------------------------------------

        self.advanced_var = tk.BooleanVar(value=False)

        ttk.Checkbutton(
            settings_frame,
            text="Enable Advanced Options",
            variable=self.advanced_var,
            command=self._toggle_advanced
        ).grid(row=3, column=0, columnspan=3, sticky="w", pady=6)

        # ------------------------------------------------------------
        # Advanced Frame
        # ------------------------------------------------------------

        self.advanced_frame = ttk.Frame(settings_frame)
        self.advanced_frame.grid(row=4, column=0, columnspan=3, sticky="w")

        self.advanced_frame.grid_remove()

        self.keep_zeros_var = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            self.advanced_frame,
            text="Keep existing zero values as zero",
            variable=self.keep_zeros_var,
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(self.advanced_frame, text="Minimum nonzero float:").grid(
            row=1, column=0, sticky="w", padx=(0, 8), pady=4
        )

        self.min_float_var = tk.StringVar(value="0.01")

        ttk.Entry(
            self.advanced_frame,
            textvariable=self.min_float_var,
            width=10
        ).grid(row=1, column=1, sticky="w")

        ttk.Label(self.advanced_frame, text="Minimum nonzero integer:").grid(
            row=2, column=0, sticky="w", padx=(0, 8), pady=4
        )

        self.min_int_var = tk.StringVar(value="1")

        ttk.Entry(
            self.advanced_frame,
            textvariable=self.min_int_var,
            width=10
        ).grid(row=2, column=1, sticky="w")

        # ------------------------------------------------------------
        # Log Window
        # ------------------------------------------------------------

        log_frame = ttk.LabelFrame(main, text="Preview / Log", padding=10)
        log_frame.pack(fill="both", expand=True, pady=(0, 10))

        self.log_text = tk.Text(log_frame, wrap="word", height=16)
        self.log_text.pack(fill="both", expand=True)

        self.log_text.insert(
            "1.0",
            "Ready.\n"
            "Adjust chaos strength, set a seed, then click Randomize and Save.\n"
        )

        self.log_text.config(state="disabled")

        # ------------------------------------------------------------
        # Buttons
        # ------------------------------------------------------------

        action_row = ttk.Frame(main)
        action_row.pack(fill="x")

        ttk.Button(
            action_row,
            text="Randomize and Save",
            command=self.randomize_and_save
        ).pack(side="left")

        ttk.Button(
            action_row,
            text="Exit",
            command=self.root.destroy
        ).pack(side="right")

    # ------------------------------------------------------------
    # Slider Label Update
    # ------------------------------------------------------------

    def _update_strength_label(self, value):

        value = float(value)

        if value < 0.2:
            level = "Very Stable"
        elif value < 0.5:
            level = "Balanced Chaos"
        elif value < 1.0:
            level = "Very Chaotic"
        else:
            level = "ABSOLUTE CHAOS"

        self.strength_label.config(text=f"{value:.2f} ({level})")

    # ------------------------------------------------------------

    def _toggle_advanced(self):

        if self.advanced_var.get():
            self.advanced_frame.grid()
        else:
            self.advanced_frame.grid_remove()

    # ------------------------------------------------------------

    def _log(self, message: str):

        self.log_text.config(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")

    # ------------------------------------------------------------
    # BYML Conversion
    # ------------------------------------------------------------

    def _run_byml_console_script(self, script_name: str, args: list[str]) -> None:
        import byml.yml_to_byml
        import sys

        old_argv = sys.argv
        try:
            sys.argv = [script_name] + args
            byml.yml_to_byml.main()
        finally:
            sys.argv = old_argv

    def _text_to_binary_byml(self, text: str) -> bytes:

        with tempfile.TemporaryDirectory() as tmpdir:

            tmp_yml = Path(tmpdir) / "temp_input.yml"
            tmp_byml = Path(tmpdir) / "temp_output.byml"

            tmp_yml.write_text(text, encoding="utf-8")

            self._run_byml_console_script(
                "yml_to_byml",
                [str(tmp_yml), str(tmp_byml)]
            )

            return tmp_byml.read_bytes()

    # ------------------------------------------------------------
    # Seed
    # ------------------------------------------------------------

    def generate_seed(self):

        seed = random.randint(100000, 999999999)

        self.seed_var.set(str(seed))

        self._log(f"Generated seed: {seed}")

    # ------------------------------------------------------------
    # Randomization Logic (UNCHANGED)
    # ------------------------------------------------------------

    def _validate_settings(self):

        try:
            strength = float(self.strength_var.get())
            min_float = float(self.min_float_var.get())
            min_int = int(self.min_int_var.get())

        except ValueError:

            messagebox.showerror(
                "Invalid Settings",
                "Strength, minimum float, and minimum integer must be valid numbers."
            )

            return None

        seed_text = self.seed_var.get().strip()

        if not seed_text:

            messagebox.showerror(
                "Missing Seed",
                "Please enter a seed or click Generate Seed."
            )

            return None

        try:
            seed = int(seed_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Seed",
                "Seed must be a valid integer."
            )

            return None

        return strength, min_float, min_int, seed

    # ------------------------------------------------------------

    def _randomize_float(self, value, strength, min_float, keep_zeros):

        if value == 0.0 and keep_zeros:
            return value

        factor = random.uniform(1.0 - strength, 1.0 + strength)

        new_value = value * factor

        if value > 0:
            return max(min_float, new_value)

        if value < 0:
            return min(-min_float, new_value)

        return min_float

    # ------------------------------------------------------------

    def _randomize_int(self, value, strength, min_int, keep_zeros):

        if value == 0 and keep_zeros:
            return value

        factor = random.uniform(1.0 - strength, 1.0 + strength)

        new_value = int(round(value * factor))

        if value > 0:
            return max(min_int, new_value)

        if value < 0:
            return min(-min_int, new_value)

        return min_int

    # ------------------------------------------------------------
    # Process PlayerConst
    # ------------------------------------------------------------

    def _process_text(self, text, strength, min_float, min_int, keep_zeros):

        lines = text.splitlines(keepends=True)

        metadata_keys = {"Version", "IsBigEndian", "SupportPaths", "HasReferenceNodes"}

        int_count = 0
        float_count = 0

        processed_lines = []

        for line in lines:

            stripped = line.strip()

            if not stripped or stripped == "root:":
                processed_lines.append(line)
                continue

            top_match = re.match(r"^([A-Za-z0-9_]+):\s*(.+)$", stripped)

            if top_match and not line.startswith(" "):

                key = top_match.group(1)

                if key in metadata_keys:
                    processed_lines.append(line)
                    continue

            int_match = re.match(r"^(\s*)([A-Za-z0-9_]+):\s*!l\s*(-?\d+)\s*$", line)

            if int_match:

                indent, key, value_str = int_match.groups()

                original = int(value_str)

                randomized = self._randomize_int(
                    original, strength, min_int, keep_zeros
                )

                processed_lines.append(f"{indent}{key}: !l {randomized}\n")

                int_count += 1

                continue

            float_match = re.match(
                r"^(\s*)([A-Za-z0-9_]+):\s*(-?\d+\.\d+)\s*$", line
            )

            if float_match:

                indent, key, value_str = float_match.groups()

                original = float(value_str)

                randomized = self._randomize_float(
                    original, strength, min_float, keep_zeros
                )

                processed_lines.append(f"{indent}{key}: {randomized:.5f}\n")

                float_count += 1

                continue

            processed_lines.append(line)

        return "".join(processed_lines), int_count, float_count

    # ------------------------------------------------------------
    # Randomize + Save
    # ------------------------------------------------------------

    def randomize_and_save(self):

        validated = self._validate_settings()

        if validated is None:
            return

        strength, min_float, min_int, seed = validated

        random.seed(seed)

        randomized_text, int_count, float_count = self._process_text(
            text=self.loaded_text,
            strength=strength,
            min_float=min_float,
            min_int=min_int,
            keep_zeros=self.keep_zeros_var.get(),
        )

        save_path = filedialog.asksaveasfilename(
            title="Save Randomized PlayerConst.byml",
            defaultextension=".byml",
            initialfile=f"PlayerConst_seed_{seed}.byml",
            filetypes=[("BYML files", "*.byml"), ("All files", "*.*")]
        )

        if not save_path:
            return

        binary_data = self._text_to_binary_byml(randomized_text)

        Path(save_path).write_bytes(binary_data)

        self._log(f"Used seed: {seed}")
        self._log(f"Saved randomized file: {save_path}")
        self._log(f"Integers changed: {int_count}")
        self._log(f"Floats changed: {float_count}")

        messagebox.showinfo(
            "Done",
            f"Randomized file saved successfully.\n\n"
            f"Seed: {seed}\n"
            f"Integers changed: {int_count}\n"
            f"Floats changed: {float_count}"
        )


def main():

    root = tk.Tk()

    try:
        style = ttk.Style()
        if "vista" in style.theme_names():
            style.theme_use("vista")
    except Exception:
        pass

    PlayerConstRandomizerApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()