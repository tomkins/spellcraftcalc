<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" indent="yes"/>
<xsl:template name="formatCost">
	<xsl:param name="cost"/>
	<xsl:variable name="plat" select="floor($cost div 10000000)"/>
	<xsl:variable name="gold" select="floor(($cost - $plat * 10000000) div 10000)"/>
	<xsl:variable name="silver" select="floor(($cost - $plat * 10000000 - $gold * 10000) div 100)"/>
	<xsl:variable name="copper" select="floor(($cost - $plat * 10000000 - $gold * 10000 - $silver * 100))"/>
	<xsl:if test="$plat &gt; 0"><xsl:copy-of select="$plat"/>p </xsl:if>
	<xsl:if test="$gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$gold"/>g </xsl:if>
	<xsl:if test="$silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$silver"/>s </xsl:if>
	<xsl:if test="$copper &gt; 0 or $silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$copper"/>c</xsl:if>
</xsl:template>

<xsl:template match="SLOT">
  <xsl:variable name="slotnum">
    <xsl:value-of select="number(@Number) + 1"/>
  </xsl:variable>
  <xsl:if test="Type != 'Unused'">
    <xsl:choose>
      <xsl:when test="@Type = 'player'">
	<label width="-1" x="5">
	  <data>
	    <xsl:text>Gem </xsl:text><xsl:copy-of select="$slotnum"/>
	    <xsl:text>: </xsl:text>
	    <xsl:value-of select="Amount"/><xsl:text> </xsl:text>
	    <xsl:value-of select="Effect"/><xsl:text> - </xsl:text>
	    <xsl:value-of select="Qua"/><xsl:text> </xsl:text>
	    <xsl:value-of select="Name"/>
	  </data>
	</label>
      </xsl:when>
      <xsl:otherwise>
	<label width="-1" x="5">
	  <data>
	    <xsl:text>Slot </xsl:text><xsl:copy-of select="$slotnum"/>
	    <xsl:text>: </xsl:text>
	    <xsl:value-of select="Amount"/><xsl:text> </xsl:text>
	    <xsl:value-of select="Effect"/>
	    <xsl:if test="@Type = 'effect'">
	      <xsl:text> - </xsl:text><xsl:value-of select="Name"/>
            </xsl:if>
	  </data>
	</label>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:if>
</xsl:template>

<xsl:template match="SCItem">
  <xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
    <label width="-1" x="5">
      <data>
	<xsl:value-of select="Location"/><xsl:text> - </xsl:text>
	<xsl:value-of select="ItemName"/>
      </data>
    </label>
    <label width="-1" x="5">
      <data>
	<xsl:text>Level: </xsl:text><xsl:value-of select="Level"/>
	<xsl:text>   Utility: </xsl:text><xsl:value-of select="Utility"/>
	<xsl:text>   Bonus: </xsl:text><xsl:value-of select="Bonus"/>
      </data>
    </label>
    <label width="-1" x="5">
      <data>
	<xsl:text>Quality: </xsl:text><xsl:value-of select="ItemQuality"/>
	<xsl:text>   AF/DPS: </xsl:text><xsl:value-of select="AFDPS"/>
	<xsl:text>   Speed: </xsl:text><xsl:value-of select="Speed"/>
      </data> 
    </label>
    <xsl:if test="ActiveState = 'player'">
      <label width="-1" x="5">
	<data>
	  <xsl:text>Imbue: </xsl:text><xsl:value-of select="Imbue"/>
	      <xsl:text> / </xsl:text><xsl:value-of select="ItemImbue"/>
	<xsl:choose>
	  <xsl:when test="Success &lt;= -100">
	    <xsl:text> - IMPOSSIBLE!</xsl:text>
	  </xsl:when>
	  <xsl:when test="Success &lt;= 0 and Success &gt; -100">
	    <xsl:text> (</xsl:text><xsl:value-of select="Success"/><xsl:text>% - BOOM!)</xsl:text>
	  </xsl:when>
	  <xsl:when test="Success &lt; 100 and Success &gt; 0">
	     <xsl:text> (</xsl:text><xsl:value-of select="Success"/><xsl:text>% Success)</xsl:text>
	  </xsl:when>
	</xsl:choose>
	<xsl:text>   Cost: </xsl:text>
	<xsl:call-template name="formatCost"><xsl:with-param name="cost" select="Cost"/></xsl:call-template>
	</data>
      </label>
    </xsl:if>

    <xsl:apply-templates select="SLOT"/>

  </xsl:if>
</xsl:template>

<xsl:template match="/SCTemplate">
  <Root_Element ID="DAOCUi">
    <WindowTemplate>

      <label width="-1" x="5"><data>Stats</data></label>
      <xsl:for-each select="Stats/*">
	<xsl:if test="name() != 'Acuity'">
	  <xsl:if test="position() = 1 or position() = 5 or position() = 10"><xsl:text disable-output-escaping="yes">&lt;label width="-1" x="5"&gt;&lt;data&gt;</xsl:text></xsl:if>
	  <xsl:choose><xsl:when test="name() = 'Hits'">Hits</xsl:when><xsl:when test="name() = 'PowerPool'">Pow%</xsl:when><xsl:otherwise><xsl:value-of select="substring(name(),1,3)"/></xsl:otherwise></xsl:choose>: <xsl:value-of select="TotalBonus"/> / <xsl:value-of select="BaseCap"/><xsl:text>   </xsl:text>
	  <xsl:if test="position() = 4 or position() = 8 or position() = last()"><xsl:text disable-output-escaping="yes">&lt;/data&gt;&lt;/label&gt;</xsl:text></xsl:if>
	</xsl:if>  
      </xsl:for-each>

      <label width="-1" x="5"><data>Resists</data></label>
      <xsl:for-each select="Resists/*">
	<xsl:if test="position() mod 3 = 1"><xsl:text disable-output-escaping="yes">&lt;label width="-1" x="5"&gt;&lt;data&gt;</xsl:text></xsl:if>
	<xsl:value-of select="name()"/>: <xsl:value-of select="TotalBonus"/> / <xsl:value-of select="BaseCap"/><xsl:text>   </xsl:text>
	<xsl:if test="position() mod 3 = 0 or position() = last()"><xsl:text disable-output-escaping="yes">&lt;/data&gt;&lt;/label&gt;</xsl:text></xsl:if>
      </xsl:for-each>

      <label x="5" width="-1"><data>Piece Listing</data></label>
      <xsl:apply-templates select="SCItem"/>

    </WindowTemplate>
  </Root_Element>
</xsl:template>

</xsl:stylesheet>
